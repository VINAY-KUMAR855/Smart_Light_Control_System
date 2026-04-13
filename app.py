import streamlit as st
import cv2
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Light Control", page_icon="💡")

st.markdown(
    "<h1 style='text-align:center;'>💡 Smart Light Control System</h1>",
    unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- SESSION STATE ----------------
if "run" not in st.session_state:
    st.session_state.run = False

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start Camera"):
        st.session_state.run = True

with col2:
    if st.button("⏹ Stop Camera"):
        st.session_state.run = False

# ---------------- PLACEHOLDERS ----------------
frame_placeholder = st.empty()

# ---------------- CAMERA ----------------
camera = cv2.VideoCapture(0)

# ---------------- LOOP ----------------
while st.session_state.run:

    success, frame = camera.read()
    if not success:
        st.error("❌ Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.1, 5)

    face_count = len(faces)

    # Draw face boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, "Face", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # ---------------- STATUS ----------------
    if face_count > 0:
        status = "LIGHT: ON"
        color = (0, 255, 0)
        bg_color = (0, 80, 0)
    else:
        status = "LIGHT: OFF"
        color = (0, 0, 255)
        bg_color = (0, 0, 80)

    # ---------------- BANNER ----------------
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 60), bg_color, -1)

    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    cv2.putText(frame, f"Faces: {face_count}",
                (frame.shape[1] - 200, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    # ---------------- DISPLAY ----------------
    frame_placeholder.image(frame, channels="BGR")

    time.sleep(0.03)

# ---------------- CLEANUP ----------------
camera.release()
