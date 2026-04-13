import streamlit as st
import cv2
import av
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.set_page_config(page_title="Smart Light Control", page_icon="💡")

st.title("💡 Smart Light Control System (Live)")

# Load face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- VIDEO PROCESSOR ----------------
class VideoProcessor(VideoTransformerBase):

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.1, 5)

        face_count = len(faces)

        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(img, "Face", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        # Status logic
        if face_count > 0:
            status = "LIGHT: ON"
            color = (0, 255, 0)
            bg_color = (0, 80, 0)
        else:
            status = "LIGHT: OFF"
            color = (0, 0, 255)
            bg_color = (0, 0, 80)

        # Banner
        cv2.rectangle(img, (0, 0), (img.shape[1], 60), bg_color, -1)

        cv2.putText(img, status, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        cv2.putText(img, f"Faces: {face_count}",
                    (img.shape[1] - 200, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        return img


# ---------------- START WEBRTC ----------------
webrtc_streamer(
    key="smart-light",
    video_transformer_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
)
