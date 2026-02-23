# 💡 Smart Light Control System
### Detect faces → Light ON | No face → Light OFF

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

## 🖥️ Setup on Ubuntu (Do this only once)

### Step 1 — Check if Python is installed
```bash
python3 --version
```
You should see something like `Python 3.10.x`. If not, install it:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

### Step 2 — Install OpenCV
```bash
pip3 install opencv-python
```

If you get a permission error, use:
```bash
pip3 install opencv-python --user
```

---

### Step 3 — Go to your project folder
```bash
cd smart_light_control
```

---

### Step 4 — Run the program
```bash
python3 main.py
```

---

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

## 🚀 Future Scope (mention this in your presentation!)
- Connect to **Arduino** to control real lights/relays
- Add **motion sensor** as backup
- Count people and log energy saved
- Send **alert notification** if lights left ON too long
