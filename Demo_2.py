import streamlit as st
import pandas as pd
import cv2
from PIL import Image

header = st.container()
imgInput,imgOutput = st.columns(2)

img = []

def mriRecon(img):
    outI = img
    return outI

def mriRecon(img):
    outI = img
    return outI

def mriRecon(img):
    outI = img
    return outI

with header:
    st.title('Multi model reconstruction Demo')


with imgInput:
    mri_k = st.file_uploader('Pick your input data')
    if mri_k is not None:
        img = Image.open(mri_k)
        st.header('Input')
        st.image(img)

with imgOutput:
    nnModel = st.selectbox('Please select the reconstruction type',['MRI Recon','X-ray Recon', 'Ultrasound Recon'])
    if nnModel is not None:
        if st.button('Reconstruct'):
            if mri_k is not None:
                if nnModel == 'MRI Recon':
                    output_img = mriRecon(img)
                    st.header('Output')
                    st.image(output_img)
                if nnModel == 'X-ray Recon':
                    st.header('Output')
                    st.image(output_img)
                if nnModel == 'Ultrasound Recon':
                    st.header('Output')
                    st.image(output_img)    


