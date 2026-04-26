import cv2
import mediapipe as mp
print("🚀 Starting Hand Gesture Recognition...")

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Start webcam
cap = cv2.VideoCapture(0)
print("👉 Press ESC to exit")
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera not working")
        break
    # Flip for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand detection
    result = hands.process(rgb)
    gesture = "No Hand"
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )
            lm = hand_landmarks.landmark

            # Finger tip indices
            tips = [4, 8, 12, 16, 20]
            fingers = []

            # Thumb (horizontal check)
            if lm[tips[0]].x < lm[tips[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers (vertical check)
            for i in range(1, 5):
                if lm[tips[i]].y < lm[tips[i] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total = sum(fingers)

          # 🎯 GESTURE CLASSIFICATION
         
            if total == 0:
                gesture = "✊ Fist"
            elif total == 1:
                gesture = "☝️ One"
            elif total == 2:
                gesture = "✌️ Peace"
            elif total == 3:
                gesture = "🤟 Three"
            elif total == 4:
                gesture = "🖖 Four"
            elif total == 5:
                gesture = "🖐️ Open Hand"

    # Display gesture on screen
    cv2.putText(frame, gesture, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Show webcam
    cv2.imshow("Hand Gesture Recognition", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        print("👋 Exiting...")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()