import streamlit as st
import time
from PIL import Image

image = Image.open('50.png')
st.image(image)

while True:
  st.balloons()
  time.sleep(5)
