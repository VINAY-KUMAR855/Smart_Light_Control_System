# ============================================================
#   Smart Light Control System
#   Detects human faces using laptop camera
#   If face detected → LIGHT ON | No face → LIGHT OFF
# ============================================================

import cv2  # OpenCV for camera and face detection

# ── Step 1: Load the face detector ──────────────────────────
# Haar Cascade is a pre-trained model that comes FREE with OpenCV
# It already knows how to detect faces — no training needed!
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# ── Step 2: Open the laptop camera ──────────────────────────
# 0 means the default built-in laptop camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("❌ Error: Could not open camera. Check if another app is using it.")
    exit()

print("✅ Camera started. Press 'Q' to quit.")

# ── Step 3: Run continuously (real-time loop) ────────────────
while True:

    # Read one frame (photo) from the camera
    success, frame = camera.read()

    if not success:
        print("❌ Failed to read from camera.")
        break

    # ── Step 4: Convert frame to grayscale ───────────────────
    # Face detection works better on grayscale images
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ── Step 5: Detect faces ─────────────────────────────────
    # scaleFactor=1.1  → checks different image sizes (catches near/far faces)
    # minNeighbors=5   → how strict the detection is (higher = less false detections)
    # minSize=(80,80)  → ignore tiny detections (noise)
    faces = face_detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    face_count = len(faces)  # how many faces found in this frame

    # ── Step 6: Draw boxes around each detected face ─────────
    for (x, y, width, height) in faces:
        # Draw green rectangle around face
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

        # Write "Face" label above the box
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # ── Step 7: Light ON/OFF logic ───────────────────────────
    if face_count > 0:
        light_status = "LIGHT: ON"
        status_color = (0, 255, 0)        # Green color (BGR format)
        bg_color     = (0, 60, 0)         # Dark green background banner
    else:
        light_status = "LIGHT: OFF"
        status_color = (0, 0, 255)        # Red color
        bg_color     = (0, 0, 80)         # Dark red background banner

    # ── Step 8: Draw status banner at the top of screen ──────
    # Draw filled rectangle as banner background
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 60), bg_color, -1)

    # Write the light status text
    cv2.putText(frame, light_status, (15, 42),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, status_color, 3)

    # Show face count on the right side of banner
    count_text = f"Faces: {face_count}"
    cv2.putText(frame, count_text, (frame.shape[1] - 150, 42),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    # ── Step 9: Show instruction text at bottom ───────────────
    cv2.putText(frame, "Press 'Q' to quit", (15, frame.shape[0] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    # ── Step 10: Display the final frame on screen ────────────
    cv2.imshow("Smart Light Control System", frame)

    # ── Step 11: Check if user pressed 'Q' to quit ───────────
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        print("👋 Exiting...")
        break

# ── Cleanup: Release camera and close all windows ────────────
camera.release()
cv2.destroyAllWindows()
print("✅ Program ended cleanly.")
