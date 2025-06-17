import cv2
import mediapipe as mp
import serial
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize serial communication with Arduino
arduino = serial.Serial('COM6', 9600)  # Change 'COM3' based on your Arduino port
time.sleep(2)  # Allow connection to establish

# Store previous positions for smooth motion
prev_positions = {"right": None}

# Function to control XYZ movement
def control_xyz(hand_landmarks):
    global prev_positions

    wrist = hand_landmarks[0]  # Wrist position
    
    if prev_positions["right"] is not None:
        dx = wrist.x - prev_positions["right"]["x"]
        dy = wrist.y - prev_positions["right"]["y"]
        dz = wrist.z - prev_positions["right"]["z"]

        movement_speed = 50  # Adjust speed sensitivity

        # Convert hand movement to robotic arm movement
        if abs(dx) > 0.01:
            arduino.write(f"X:{int(dx * movement_speed)}\n".encode())  # Move X-axis
        if abs(dy) > 0.01:
            arduino.write(f"Y:{int(dy * movement_speed)}\n".encode())  # Move Y-axis
        if abs(dz) > 0.01:
            arduino.write(f"Z:{int(dz * movement_speed)}\n".encode())  # Move Z-axis

    prev_positions["right"] = {"x": wrist.x, "y": wrist.y, "z": wrist.z}

# Function to detect gripper gestures
def detect_gripper_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Open Hand Gesture → Open Gripper
    if (index_tip.y < landmarks[6].y and middle_tip.y < landmarks[10].y and
        ring_tip.y < landmarks[14].y and pinky_tip.y < landmarks[18].y):
        return "open_gripper"

    # Closed Fist Gesture → Close Gripper
    if (index_tip.y > landmarks[6].y and middle_tip.y > landmarks[10].y and
        ring_tip.y > landmarks[14].y and pinky_tip.y > landmarks[18].y):
        return "close_gripper"

    return None

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = "right" if handedness.classification[0].label == "Right" else "left"

            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if hand_label == "right":
                control_xyz(hand_landmarks.landmark)  # Right hand controls XYZ movement
            elif hand_label == "left":
                gripper_action = detect_gripper_gesture(hand_landmarks.landmark)
                if gripper_action == "open_gripper":
                    arduino.write(b"G:OPEN\n")  # Open Gripper
                elif gripper_action == "close_gripper":
                    arduino.write(b"G:CLOSE\n")  # Close Gripper

    cv2.imshow('Gesture Control - XYZ Positioning + Gripper', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
arduino.close()
