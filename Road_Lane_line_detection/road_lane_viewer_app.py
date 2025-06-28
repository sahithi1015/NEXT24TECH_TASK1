import streamlit as st
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# --- CONFIGURATION ---
# Set the dataset base path here
DATASET_PATH = r"C:/Users/sahit/OneDrive/Documents/Desktop/internships/Next24tech/road_lane"
IMAGE_FOLDER = os.path.join(DATASET_PATH, 'train', 'images')
LABEL_FOLDER = os.path.join(DATASET_PATH, 'train', 'labels')

# --- STREAMLIT UI ---
st.set_page_config(page_title="Lane Detection Viewer", layout="centered")
st.title("🚦 Lane Detection Visualizer")

# Load available images
if not os.path.exists(IMAGE_FOLDER):
    st.error("Image folder not found.")
else:
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.jpg', '.png'))]
    selected_image_file = st.selectbox("Choose an image from dataset", image_files)

    if selected_image_file:
        image_path = os.path.join(IMAGE_FOLDER, selected_image_file)
        label_file = os.path.splitext(selected_image_file)[0] + '.txt'
        label_path = os.path.join(LABEL_FOLDER, label_file)

        # Load image
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        lane_image = image.copy()
        height, width, _ = image.shape

        lanes = []
        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                for line in f:
                    coords = list(map(float, line.strip().split()[1:]))  # skip lane ID
                    points = [(int(coords[i] * width), int(coords[i+1] * height)) for i in range(0, len(coords), 2)]
                    lanes.append(points)

            # Draw lanes
            colors = [(0, 165, 255), (255, 127, 0), (0, 255, 0), (255, 0, 255)]
            for i, lane in enumerate(lanes):
                for j in range(len(lane) - 1):
                    cv2.line(lane_image, lane[j], lane[j+1], colors[i % len(colors)], 5)

            # Show side-by-side using PIL for compatibility
            st.subheader("Comparison View")
            col1, col2 = st.columns(2)

            with col1:
                st.image(image, caption="Original Image", use_container_width=True)

            with col2:
                st.image(lane_image, caption="Detected Lanes", use_container_width=True)
        else:
            st.warning("No label file found for this image.")
