# Aerial Plane Detector (YOLOv8)

**Team:** Kernel Ninjas  
**Team Lead:** Mabo Giqwa  
**Teammates:** Dr San Sahasra, Siphelele Ndlovu, Sello Serutle, Fortune Mkhwebane

## Team Photo

![Kernel Ninjas Team Photo](./images/team.PNG)

## Overview
This project is an aerial imagery aircraft detection system built for the **inaugural UNISA Hackathon**. The solution uses a **YOLOv8** object detection model trained on the **DOTA v1.0** dataset to detect planes in aerial images. The application is deployed using **Hugging Face Spaces** as the backend and presented via a simple web interface.

Hackathon reference: UNISA hosts first-ever Hackathon to ignite student learning experience.

## Demo
The web UI embeds the deployed Hugging Face Space and allows users to upload aerial imagery for inference.

## Website
Live demo: [https://mabogiqwa.github.io/Aerial-ML/](https://mabogiqwa.github.io/Aerial-ML/)

## Model & Training
- **Architecture:** YOLOv8
- **Dataset:** DOTA v1.0 (aerial object detection dataset)
- **Training platform:** Google Colab
- **Accelerator:** TPUs
- **Data split used:**
  - Train: **1,302 images**
  - Validation: **109 files**

The model was initially trained in Google Colab using TPUs for faster experimentation and iteration.

## System Architecture
- **Backend:** Hugging Face Spaces (serving the YOLOv8 model for inference)
- **Frontend:** Lightweight HTML page embedding the Space via an iframe
- **Inference flow:**
  1. User uploads an aerial image via the web UI.
  2. The request is forwarded to the Hugging Face Space backend.
  3. YOLOv8 performs object detection.
  4. The annotated result is returned to the user.

## Repository Structure (example)
```
.
├── index.html        # Frontend UI embedding the Hugging Face Space
├── (training)        # Notebooks / scripts used for training (if included)
├── (inference)       # Inference or app code for Hugging Face Spaces
└── README.md
```

## How to Run Locally (Frontend)
1. Clone the repository.
2. Open `index.html` in your browser.
3. The page will load the Hugging Face Space in an iframe for live inference.

> Note: The model itself is served via Hugging Face Spaces, so no local GPU/TPU setup is required just to use the demo UI.

## Reproducibility (Training)
To reproduce training:
- Prepare the **DOTA v1.0** dataset in YOLO format.
- Use **YOLOv8** training scripts/notebooks in Google Colab.
- Configure Colab to use **TPUs**.
- Set the train/val splits similar to:
  - Train: 1,302 images
  - Val: 109 files

## Use Cases
- Monitoring airfields from aerial or satellite imagery
- Dataset exploration and benchmarking on aerial object detection
- Educational demonstration of end-to-end ML deployment (training → serving → web UI)

## Acknowledgements
- **UNISA Hackathon** for hosting the event and providing the platform for this project.
- **DOTA Dataset** creators for the aerial imagery dataset.
- **Ultralytics YOLOv8** for the detection framework.
- **Hugging Face Spaces** for model hosting and deployment.

## License
Open Source

