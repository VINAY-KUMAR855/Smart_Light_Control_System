# 💡 Smart Light Control System
### A system that uses your laptop camera to detect if anyone is in the room → if yes, lights ON; if no one, lights OFF. Status is displayed on screen.

---

## 📁 Folder Structure

```
smart_light_control/
│
├── main.py             ← Main program (run this)
├── requirements.txt    ← Python libraries needed
└── README.md           ← This file
```

---
## How It Works
Camera → Detect Face → Decision → Display Status on Screen

  📷         🧠           💡              🖥️
  
the "light ON/OFF" will be simulated on screen with text and colors

![Working](Overview_image.png)
## Tools You'll Use
Python is your language. Three main libraries:
- OpenCV — accesses camera, detects faces, shows video
- Haar Cascade — a pre-trained face detector (comes free with OpenCV, no training needed)
- No internet needed, no GPU needed — runs on any basic laptop



## 🎮 How to Use

| Action | Result |
|--------|--------|
| Sit in front of camera | Green box appears, **LIGHT: ON** shown |
| Leave camera view | **LIGHT: OFF** shown in red |
| Press `Q` | Program exits |

---

## ❌ Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `Could not open camera` | Close browser/Zoom that might be using camera |
| `No module named cv2` | Run `pip3 install opencv-python` again |
| Camera opens but no face detected | Make sure your face is well lit, move closer |

---

## 🚀 Future Scope
- Connect to **Arduino** to control real lights/relays
- Add **motion sensor** as backup
- Count people and log energy saved
- Send **alert notification** if lights left ON too long
