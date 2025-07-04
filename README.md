# NEXT24TECH
AIML internship
## Task 1
# 🛣️ Road Lane Line Detection System

## 🔍 Project Overview
The **Road Lane Line Detection System** is a computer vision-based project designed to enhance road safety by accurately detecting lane markings in real time. This system helps assist autonomous driving and driver-assistance technologies by identifying road lanes under various conditions.

---

## 🧠 Key Objectives

-  Detect lane lines from real-time or recorded video/image input.
-  Improve driver assistance by providing visual guidance.
-  Research and implement **state-of-the-art lane detection algorithms** (e.g., Canny Edge Detection, Hough Transform, Deep Learning-based models).
-  Test model performance under diverse scenarios (e.g., daylight, shadows, rainy weather, curved roads).



## Road Lane Line Detection System 
This project is a Streamlit-based interactive viewer for visualizing annotated road lane lines from a dataset. It allows users to select images from a training set.

---

## 📊 Dataset Info

- **Dataset Used**: [Lane Detection - Road Line Detection Image Dataset (Kaggle)](https://www.kaggle.com/datasets/dataclusterlabs/lane-detection-road-line-detection-image-dataset)
- **Content**:
  - Train and Test images of road scenarios
  - Labeled lane lines for supervised learning tasks
- **Use**: Helps train/test the accuracy of lane detection algorithms

---

## ⚙️ Technologies Used

- **Programming Language**: Python 
- **Libraries**:
  - OpenCV (image processing)
  - NumPy (array handling)
  - Matplotlib (visualization)
  - TensorFlow 
- **Optional**:
  - streamlit for creating a live demo web interface

---

## 🚦 Detection Pipeline

1. **Input Frame**: Road image or video frame is captured.
2. **Preprocessing**: Convert to grayscale, apply Gaussian blur.
3. **Edge Detection**: Use Canny edge detection.
4. **Region of Interest**: Mask the region where lanes are expected.
5. **Line Detection**: Apply Hough Transform or ML model.
6. **Overlay**: Detected lanes are drawn and returned as output.

---

## 🎥 Demo

- Input: road image
- Output: Lane lines marked on the road in real-time

---

## 🚀 Future Enhancements

-  Integrate with dashcam input for live processing
-  Improve detection under poor visibility (rain, snow, fog)
-  Deep learning-based segmentation (e.g., using U-Net, YOLO)
-  GPS and lane mapping integration
-  Android/iOS app for mobile deployment

---

### Features:
 
* Select an image from the dataset's training folder.

* Parse lane annotations from label files (.txt) and project them on the image.

* Overlay detected lanes with distinct colors for better visualization.

* Side-by-side comparison between the original and detected lane images.

---

  ### Output Images:

  

![image](https://github.com/user-attachments/assets/fbab7e8f-d0ab-48dc-96e9-37dc9d482217)




![image](https://github.com/user-attachments/assets/b70f2c65-db44-40dc-9d22-020c2aa17929)


