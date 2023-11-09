import streamlit as st
import pandas as pd
from PIL import Image

sidebar = st.sidebar

sidebar.header('Side Heading')
name_input = sidebar.text_input("Enter Your Name : ")
btn1 = sidebar.button('Click me')

st.title('Video Games Sales Analysis')

st.markdown("""
## Level 2 Heading
""")

if name_input:
    st.subheader('Your name is :'+name_input)

df = pd.read_csv('dataset.csv')
st.dataframe(df)

img = st.file_uploader('Insert Image Here')

if img:
    st.image(Image.open(img))