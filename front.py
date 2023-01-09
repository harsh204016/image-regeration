import streamlit as st
import requests
import json
import numpy as np

#image
from config import STYLES , generate_style
from PIL import Image
from io import BytesIO
import base64

st.set_option("deprecation.showfileUploaderEncoding", False)

# st.markdown('<style>body{background-color: blue;}</style>',unsafe_allow_html=True)
# st.sidebar.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
# defines an h1 header
st.sidebar.title("Style Transfer")

# displays a file uploader widget
image = st.sidebar.file_uploader("Choose an image",)



st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# displays the select widget for the styles
style = st.sidebar.radio("Select your style", [i for i in STYLES.keys()])
#style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

# displays a button
if st.sidebar.button("Style Transfer"):
    if image is not None and style is not None:
        

        col1,col2 = st.columns(2)
        with col1:
            st.image(image)
        with col2:
            
            with st.spinner('Applying Magic'):
                style_image = generate_style(style,image)
            st.image(style_image)
        
        print(type(style_image))

        
        random_array = np.random.random_sample(style_image.shape) * 255
        random_array = random_array.astype(np.uint8)
        result = Image.fromarray(random_array)

        def get_image_download_link(img):
            """Generates a link allowing the PIL image to be downloaded
            in:  PIL image
            out: href string
            """
            buffered = BytesIO()
            img.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
            return href

        st.markdown(get_image_download_link(result), unsafe_allow_html=True)
        

    





