# ✋ Hand Gesture Recognition using OpenCV & MediaPipe

## 🚀 Project Overview

This project implements a **real-time hand gesture recognition system** using a webcam. It detects hand landmarks and classifies basic gestures like fist, open hand, and finger counts.

The system uses:
* OpenCV for video processing
* MediaPipe for hand tracking

## 🎯 Features
* 📷 Real-time webcam detection
* ✋ Detects single hand
* 🤖 Recognizes gestures:

  * ✊ Fist
  * ☝️ One
  * ✌️ Peace
  * 🤟 Three
  * 🖖 Four
  * 🖐️ Open Hand
* 🟢 Displays gesture label on screen

## 🧠 How It Works
1. Webcam captures live video
2. Frames are converted to RGB
3. MediaPipe detects hand landmarks
4. Finger positions are analyzed
5. Gesture is classified based on number of fingers raised

## ⚙️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition
```
### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
```bash
pip install opencv-python mediapipe==0.10.9
```

## 🎮 Controls
* Press **ESC** → Exit application

## ⚠️ Requirements for Best Performance
* Good lighting 💡
* Clear background
* Hand fully visible in frame
* Keep hand centered

## 📸 Output
* Webcam window opens
* Hand landmarks drawn
* Gesture name displayed in real-time

## 🧩 Technologies Used
* Python
* OpenCV
* MediaPipe

## 🚧 Limitations
* Works best with one hand
* Limited gesture set
* Accuracy depends on lighting and hand visibility

## 🚀 Future Improvements
* Add custom gesture training
* Control system (volume, mouse, etc.)
* Multi-hand detection
* GUI interface
