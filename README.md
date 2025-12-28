# SurgiMind 🧠🔬
AI-powered Surgical Tool Detection using YOLOv8

⚠️ **Sensitive Content Warning**  
This project processes laparoscopic surgical videos intended strictly for research and educational purposes.

---

## 🚀 Project Overview

SurgiMind is an end-to-end computer vision system for detecting surgical tools in laparoscopic videos.

### Current Version: **v1**
- Object Detection (Bounding Boxes + Tool Names)
- Confidence score tracking
- Video-level inference
- Web-based UI (upload → detect → download)

---

## 🧠 Model Details

- **Architecture:** YOLOv8 (Nano)
- **Layers:** 72
- **Trainable Parameters:** ~3.7 million
- **Compute:** ~8.1 GFLOPs
- **Training Time:** ~33.07 hours
- **Hardware:** Apple MacBook M3 (CPU-only, no GPU)

---

## 🧪 Dataset

- **CholecTrack20**
- Annotated laparoscopic surgery videos
- Tools detected in v1:
  - Grasper
  - Hook
  - Scissors
  - Clip Applier
  - Bipolar
  - Irrigator

---

## 📊 Model Metrics (v1)

- **Precision:** High for dominant tools
- **Recall:** Stable across tested videos
- **mAP@0.5:** Consistent on validation set
- **Inference Speed:** ~60–75 ms per frame (CPU)

---

## 🌐 System Architecture

Frontend (HTML/CSS/JS)
↓
FastAPI Backend
↓
YOLOv8 Inference
↓
Annotated Video Output


---

## 🧩 Version 2 (Coming Next)

- Full dataset fine-tuning (all remaining CholecTrack20 annotations)
- Improved accuracy & reduced false positives
- Tool-action awareness
- Temporal consistency
- Optional cloud GPU training

---

## ⚠️ Disclaimer

This system is **not for clinical decision-making**.  
Research and demonstration purposes only.

---

## 👤 Author

Built by **Sofiyaan Mohammed**  
B.Tech CSE | Computer Vision | AI Systems
