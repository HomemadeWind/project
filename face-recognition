import numpy as np
import cv2
import streamlit as st
from deepface import DeepFace
st.text("Name")
name = st.text_input('Text input', 'Default')
run = st.camera_input("Take photo")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
ten=["phong","van"]
verify=["phong.jpg","van.jpg"]
while True:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    if run:
        result = DeepFace.verify(img1_path = st.image(run) , img2_path = verify[np.where(name==ten)])
