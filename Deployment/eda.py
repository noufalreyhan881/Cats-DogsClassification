import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def run():
    st.title('Welcome to Explaration Data Analysis')

    st.title('Class Image')

    image = Image.open('EDA1.png')
    st.image(image, caption='Cats and Dogs classification')
    with st.expander('Explanation'):
        st.caption('Menampilkan Gambar')