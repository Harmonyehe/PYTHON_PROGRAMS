import cv2
import mediapipe as mp
import serial
import time
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize serial communication with Arduino
arduino = serial.Serial('COM6', 9600)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Wait for the connection to establish

# Robot arm parameters (in mm)
L1 = 100  # Length of the first arm segment (shoulder to elbow)
L2 = 100  # Length of the second arm segment (elbow to wrist)
L3 = 50   # Length of the third arm segment (wrist to gripper)

# Function to calculate inverse kinematics for 6-DOF arm (including gripper)
def inverse_kinematics(x, y, z):
    # Calculate base angle (rotation around Z-axis)
    base_angle = math.degrees(math.atan2(y, x))

    # Calculate distance in the X-Y plane
    xy_distance = math.sqrt(x**2 + y**2)

    # Calculate shoulder and elbow angles using simplified 2D inverse kinematics
    D = (xy_distance**2 + z**2 - L1**2 - L2**2) / (2 * L1 * L2)
    
    # Clamp D to [-1, 1] to prevent math domain error
    D = max(-1, min(1, D))  # Ensure D is within the valid range
    
    elbow_angle = math.degrees(math.atan2(math.sqrt(1 - D**2), D))
    shoulder_angle = math.degrees(math.atan2(z, xy_distance) - math.atan2(L2 * math.sin(math.radians(elbow_angle)), L1 + L2 * math.cos(math.radians(elbow_angle))))

    # Calculate wrist position (gripper position can be controlled based on wrist)
    wrist_x = x
    wrist_y = y
    wrist_z = z - L3  # The gripper's Z position is offset from the wrist position

    gripper_angle = 90  # Default gripper angle (neutral position)

    return base_angle, shoulder_angle, elbow_angle, wrist_x, wrist_y, wrist_z, gripper_angle

# Function to detect gestures
def detect_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Check for open hand (all fingers extended)
    if (index_tip.y < landmarks[6].y and middle_tip.y < landmarks[10].y and
        ring_tip.y < landmarks[14].y and pinky_tip.y < landmarks[18].y):
        return "open_hand"

    # Check for closed fist (all fingers folded)
    if (index_tip.y > landmarks[6].y and middle_tip.y > landmarks[10].y and
        ring_tip.y > landmarks[14].y and pinky_tip.y > landmarks[18].y):
        return "closed_fist"

    # Check for pointing gesture (index finger extended)
    if index_tip.y < landmarks[6].y and middle_tip.y > landmarks[10].y and ring_tip.y > landmarks[14].y and pinky_tip.y > landmarks[18].y:
        return "pointing"

    # Check for thumb up gesture
    if thumb_tip.y < landmarks[2].y and index_tip.y > landmarks[6].y and middle_tip.y > landmarks[10].y:
        return "thumb_up"

    # Check for thumb down gesture
    if thumb_tip.y > landmarks[2].y and index_tip.y > landmarks[6].y and middle_tip.y > landmarks[10].y:
        return "thumb_down"

    return None

# Function to send servo commands based on XYZ position and gesture
def send_servo_command(x, y, z, gesture):
    # Calculate joint angles using inverse kinematics
    base_angle, shoulder_angle, elbow_angle, wrist_x, wrist_y, wrist_z, gripper_angle = inverse_kinematics(x, y, z)

    # Send joint angles to Arduino
    arduino.write(f"0:{base_angle}\n1:{shoulder_angle}\n2:{elbow_angle}\n3:{wrist_x}\n4:{wrist_y}\n5:{wrist_z}\n6:{gripper_angle}\n".encode())

    # Control gripper based on gesture
    if gesture == "open_hand":
        arduino.write(b"7:0\n")  # Open gripper
    elif gesture == "closed_fist":
        arduino.write(b"7:180\n")  # Close gripper
    elif gesture == "pointing":
        arduino.write(b"7:90\n")  # Neutral position for gripper
    elif gesture == "thumb_up":
        arduino.write(b"7:45\n")  # Gripper slightly open
    elif gesture == "thumb_down":
        arduino.write(b"7:135\n")  # Gripper slightly closed

# Function to send the robot arm to the home position
def move_to_home_position():
    # Send the robot arm to the home position (base = 0°, shoulder = 0°, elbow = 0°, gripper = 90°)
    arduino.write(b"0:0\n1:0\n2:0\n3:0\n4:0\n5:0\n6:90\n")  # All motors to home position
    arduino.write(b"7:90\n")  # Gripper to neutral position
    time.sleep(1)  # Wait for the arm to move to home position

# Initialize the arm in the home position
move_to_home_position()

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect gesture
            gesture = detect_gesture(hand_landmarks.landmark)

            # Get hand position (X, Y, Z)
            wrist = hand_landmarks.landmark[0]  # Use wrist landmark as reference
            x = int(wrist.x * frame.shape[1])  # X coordinate in pixels
            y = int(wrist.y * frame.shape[0])  # Y coordinate in pixels
            z = int(wrist.z * 1000)  # Z coordinate (scaled)

            # Map hand position to robot arm workspace (adjust scaling as needed)
            x_mm = int((x / frame.shape[1]) * 200)  # Map X to 0-200 mm
            y_mm = int((y / frame.shape[0]) * 200)  # Map Y to 0-200 mm
            z_mm = int((z / 1000) * 200)  # Map Z to 0-200 mm

            # Send servo commands
            send_servo_command(x_mm, y_mm, z_mm, gesture)

            # Debugging: Print calculated angles and gesture
            print(f"Base: {x_mm}, Shoulder: {y_mm}, Elbow: {z_mm}, Gesture: {gesture}")

    # Display the frame
    cv2.imshow('Gesture Control', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
arduino.close()
