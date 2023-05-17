import numpy as np
import cv2
import streamlit as st
from deepface import DeepFace
# st.text("Name")
# name = st.text_input('Text input', 'Default')
# # run = st.checkbox('Run')
# # FRAME_WINDOW = st.image([])
# # camera = cv2.VideoCapture(0)

# # while run:
# #     _, frame = camera.read()
# #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #     FRAME_WINDOW.image(frame)
# # else:
# #     st.write('Stopped')

# run = st.camera_input("Take photo")
# FRAME_WINDOW = st.image([])
# camera = cv2.VideoCapture(0)
# ten=["phong","van"]
# verify=["phong.jpg","van.jpg"]
# while True:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
#     if run:
#         # veri=DeepFace.find(img_path = run, db_path = "D:/pic")
#         result = DeepFace.verify(img1_path = st.image(run) , img2_path = verify[np.where(name==ten)])
        
            
    

    
# def recog():
#     info = DeepFace.find(img_path="Messi_vs_Nigeria_2018.jpg" , db_path="D:/pic")
#     print("info")
def camera():
    DeepFace.stream(db_path="D:/pic")
camera()