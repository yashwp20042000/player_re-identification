# 🏃‍♂️ Player Re-Identification in a Single Feed 🎥

This project detects and re-identifies players in a single video feed using a YOLOv11 object detection model. It assigns consistent player IDs even if players temporarily leave and re-enter the frame.

---

## 📂 Project Structure

player_re-identification
├── detect_and_track.py # Main script for detection and tracking
├── models/
│ └── best.pt # YOLOv11 trained model (handled via Git LFS)
├── video/
│ └── 15sec_input_720p.mp4 # Input video file
├── output/
│ └── output.mp4 # Output video with tracking (generated)
├── requirements.txt
└── README.md


---

## ⚙️ Requirements

- Python **3.8 - 3.12**  
- Recommended: Virtual Environment  
- Git with **Git LFS** (for large model file handling)  

---

## 📦 Dependencies

Install the following packages:

opencv-python
ultralytics
numpy

---

## 🖥️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yashwp20042000/player_re-identification.git
cd player_re-identification
```

2️⃣ Install Git LFS (if not installed)

```bash
git lfs install
git lfs pull
```

3️⃣ Create & Activate Virtual Environment (Recommended)

```bash
python -m venv .venv
```

4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

5️⃣ Add the Model File

If model not present, download manually:
https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view

Place best.pt inside:
models/best.pt

6️⃣ Place the Input Video

Put 15-second input video:
https://drive.google.com/file/d/1TDcND31fvEDvcnZCaianTxJrmT8q7iIi/view?usp=drive_link

▶️ Run the Code

~~~bash
python detect_and_track.py
~~~

The output video with re-identified players will be saved in:
output/output.mp4

🎯 Features

✔ Player detection using YOLOv11
✔ Consistent player IDs even after leaving/re-entering frame
✔ Real-time simulation with OpenCV display
✔ Output video with player tracking overlay

❗ Troubleshooting

Ensure models/best.pt exists
If Git LFS fails, download model manually
Use cv2.COLOR_BGR2RGB conversion for correct frame processing
For performance issues, reduce video resolution or skip frames

