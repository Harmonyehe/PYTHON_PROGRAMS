import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize OpenCV
cap = cv2.VideoCapture(0)  # Use webcam
canvas = None  # Canvas to draw on
prev_x, prev_y = 0, 0  # Previous coordinates of the index finger

# Colors and tools
colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]  # Green, Blue, Red, Yellow
current_color = colors[0]  # Default color
eraser_mode = False  # Eraser mode flag

def get_finger_status(hand_landmarks):
    """Check if fingers are up or down."""
    tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []

    # Thumb (check if it's to the left or right of the hand)
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)  # Thumb is up
    else:
        fingers.append(0)  # Thumb is down

    # Other fingers
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers.append(1)  # Finger is up
        else:
            fingers.append(0)  # Finger is down

    return fingers

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Get the frame dimensions
    height, width, _ = frame.shape

    # Initialize the canvas if it hasn't been initialized yet
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of the index finger tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * width), int(index_finger_tip.y * height)

            # Check finger status
            fingers = get_finger_status(hand_landmarks)

            # Change color based on finger status
            if fingers[1] and not any(fingers[2:]):  # Only index finger up
                current_color = colors[0]  # Green
                eraser_mode = False
            elif fingers[1] and fingers[2] and not any(fingers[3:]):  # Index and middle fingers up
                current_color = colors[1]  # Blue
                eraser_mode = False
            elif fingers[1] and fingers[2] and fingers[3] and not fingers[4]:  # Index, middle, ring fingers up
                current_color = colors[2]  # Red
                eraser_mode = False
            elif fingers[1] and fingers[2] and fingers[3] and fingers[4]:  # All fingers up
                current_color = colors[3]  # Yellow
                eraser_mode = False
            elif not any(fingers[1:]):  # Fist (no fingers up)
                eraser_mode = True  # Activate eraser

            # Draw or erase on the canvas
            if prev_x != 0 and prev_y != 0:
                if eraser_mode:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 0, 0), 20)  # Erase (draw black)
                else:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), current_color, 5)  # Draw with selected color

            prev_x, prev_y = x, y

    # Combine the canvas and the frame
    frame = cv2.addWeighted(frame, 1, canvas, 1, 0)

    # Display the current color and eraser status
    cv2.putText(frame, f"Color: {current_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    if eraser_mode:
        cv2.putText(frame, "Eraser Mode", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow("Gesture-Based Drawing", frame)

    # Clear the canvas when 'c' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas = np.zeros_like(frame)

    # Exit when 'q' is pressed
    if key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()