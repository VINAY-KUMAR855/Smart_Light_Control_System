import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Smart Light Control", page_icon="💡")

st.title("💡 Smart Light Control System")

# Load face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 📸 Take image from camera
image = st.camera_input("Take a photo")

if image is not None:

    # Convert to OpenCV format
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(gray, 1.1, 5)
    face_count = len(faces)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, "Face", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # Status
    if face_count > 0:
        status = "LIGHT: ON"
        color = (0,255,0)
        bg_color = (0,80,0)
    else:
        status = "LIGHT: OFF"
        color = (0,0,255)
        bg_color = (0,0,80)

    # Banner
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 60), bg_color, -1)

    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    cv2.putText(frame, f"Faces: {face_count}",
                (frame.shape[1] - 200, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    # Show result
    st.image(frame, channels="BGR")
