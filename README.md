# 🚦 Traffic Violation Detection System

A computer vision-based traffic violation detection system built using **Python, YOLO, and OpenCV**.

The system analyzes traffic video footage and detects motorcycle-related traffic violations. The current version focuses on:

* 🪖 **No Helmet Detection**
* 👥 **Triple Riding Detection**
* 🏍️ **Motorcycle & Rider Detection**
* 🔢 **Number Plate Detection** — planned for the next module

---

## 📌 Project Overview

The goal of this project is to use computer vision and object detection to automatically identify common traffic violations from video footage.

The system processes a traffic video frame-by-frame and uses multiple YOLO models to detect motorcycles, people, and helmet status.

### Current Pipeline

```text
Traffic Video
      │
      ▼
Vehicle Detection
      │
      ├── Person Detection
      └── Motorcycle Detection
                │
                ▼
        Rider Association
                │
                ▼
        Helmet Detection
                │
                ├── With Helmet
                └── Without Helmet
                │
                ▼
       Violation Detection
                │
                ├── No Helmet
                └── Triple Riding
```

---

## ✨ Features

### 🏍️ Motorcycle Detection

The system detects motorcycles using a YOLO object detection model.

Each detected motorcycle is processed individually.

### 👤 Rider Detection

People detected around motorcycles are associated with nearby motorcycles to determine the number of riders.

### 👥 Triple Riding Detection

If a motorcycle is associated with **3 or more riders**, the system identifies it as a triple-riding violation.

Example:

```text
Riders : 3
TRIPLE RIDING
```

### 🪖 Helmet Detection

A separate YOLO model is used to detect helmet status.

The helmet model contains two classes:

```text
0 → With helmet
1 → Without helmet
```

If a rider is detected without a helmet, the motorcycle is marked with a **NO HELMET** violation.

### 🚨 Multiple Violations

A motorcycle can be identified with multiple violations simultaneously.

For example:

```text
Riders : 3
TRIPLE RIDING
NO HELMET
```

---

# 🛠️ Tech Stack

* **Python 3.11**
* **YOLO / Ultralytics**
* **OpenCV**
* **NumPy**
* **EasyOCR** *(planned for number plate recognition)*

---

# 📂 Project Structure

```text
traffic-violation-system/
│
├── main.py
├── detector.py
├── association.py
├── vehicle.py
├── helmet.py
├── visualizer.py
│
├── models/
│   ├── vehicle.pt
│   └── helmet.pt
│
├── videos/
│   └── traffic.mp4
│
├── outputs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧠 Project Architecture

The project is divided into multiple modules so that each component has a specific responsibility.

### `main.py`

The main entry point of the application.

It:

1. Reads the traffic video.
2. Runs vehicle detection.
3. Runs helmet detection.
4. Extracts people and motorcycles.
5. Associates riders with motorcycles.
6. Associates helmet detections.
7. Sends the results to the visualizer.

---

### `detector.py`

Responsible for loading and running the YOLO models.

Currently it loads:

```text
models/vehicle.pt
models/helmet.pt
```

The vehicle model performs tracking using **ByteTrack**.

---

### `association.py`

Responsible for associating detected people with motorcycles.

The system uses the position of a person relative to a motorcycle to determine whether that person is likely to be a rider.

---

### `vehicle.py`

Contains the `Vehicle` class.

Each detected motorcycle is represented as a `Vehicle` object containing information such as:

```python
vehicle.riders
vehicle.rider_count
vehicle.triple_riding
vehicle.with_helmet
vehicle.without_helmet
vehicle.number_plate
```

This allows information related to a motorcycle to stay together.

---

### `helmet.py`

Responsible for associating helmet detections with detected motorcycles.

The helmet model predicts:

```text
With helmet
Without helmet
```

The result is then stored in the corresponding `Vehicle` object.

---

### `visualizer.py`

Responsible for drawing the final results on the video.

The system intentionally does not use YOLO's default `.plot()` output so that the final interface remains clean.

Example:

```text
┌─────────────────────┐
│ Riders : 3          │
│ TRIPLE RIDING       │
│ NO HELMET           │
└─────────────────────┘
```

---

# ⚙️ Installation

## 1. Prerequisites

Make sure you have:

* Python 3.11 recommended
* Git
* A computer capable of running YOLO inference

Check Python:

```bash
python --version
```

Recommended:

```text
Python 3.11.x
```

---

# 2. Clone the Repository

```bash
git clone https://github.com/asad121212/traffic-violation-system.git
```

Enter the project directory:

```bash
cd traffic-violation-system
```

---

# 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

You should see something similar to:

```text
(venv) PS D:\traffic-violation-system>
```

---

# 4. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs the required Python packages.

---

# 🎥 5. Add a Traffic Video

Place your traffic video inside:

```text
videos/
```

The current code expects the video to be named:

```text
traffic.mp4
```

Therefore:

```text
videos/
└── traffic.mp4
```

> The sample traffic video is not included in the repository. You can use your own traffic footage for testing.

---

# ▶️ 6. Run the Project

Make sure your virtual environment is activated.

Then:

```bash
python main.py
```

A window named:

```text
Traffic Violation Detection
```

will open.

Press:

```text
ESC
```

to stop the application.

---

# 📦 Models

The project currently uses two YOLO models:

```text
models/
├── vehicle.pt
└── helmet.pt
```

### Vehicle Model

Used for detecting:

* Person
* Motorcycle

and tracking detected objects using ByteTrack.

### Helmet Model

Used for detecting:

```text
With helmet
Without helmet
```

---

# 🚨 Violation Detection

## No Helmet

A motorcycle is flagged when a rider is associated with a:

```text
Without helmet
```

detection.

Output:

```text
NO HELMET
```

---

## Triple Riding

A motorcycle is flagged when:

```text
rider_count >= 3
```

Output:

```text
TRIPLE RIDING
```

---

# 🔮 Future Improvements

The project is currently under development.

Planned features include:

### 🔢 Number Plate Detection

Add a dedicated YOLO number plate detection model.

```text
Motorcycle
     ↓
Number Plate
     ↓
Plate Crop
```

### 🔤 Number Plate Recognition

Use OCR to extract the registration number.

```text
Number Plate
     ↓
EasyOCR
     ↓
CG04AB1234
```

### 📸 Violation Evidence

Automatically save an image when a violation is detected.

Example:

```text
outputs/
├── violation_001.jpg
├── violation_002.jpg
└── violation_003.jpg
```

### 🕐 Timestamp

Store the time at which the violation occurred.

### 🗃️ Violation Records

Store information such as:

```text
Violation Type
Number Plate
Timestamp
Image
```

in a CSV/database.

### 🎯 Improved Object Association

Improve rider and helmet association using:

* Tracking IDs
* Rider-to-bike matching
* Spatial relationships
* Temporal consistency

---

# ⚠️ Current Limitations

The current system is a prototype and may produce incorrect detections in certain situations.

Possible issues include:

* Small/distant motorcycles may be harder to detect.
* Helmet detection accuracy depends on the training data of the helmet model.
* Nearby motorcycles may cause incorrect rider/helmet association.
* Crowded traffic can cause incorrect rider counts.
* Poor lighting and low-resolution footage can reduce detection accuracy.

These limitations are being addressed as development continues.

---

# 👨‍💻 Development

The project is being developed as a college mini-project focused on applying **Computer Vision and Object Detection** to traffic monitoring.

The architecture is intentionally modular so that additional traffic violations and detection models can be added without rewriting the entire application.

---

# 📜 License

This project is intended for educational and academic purposes.
