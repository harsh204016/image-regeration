import streamlit as st
import requests
import json
import numpy as np

#image
from config import STYLES , generate_style 
from PIL import Image

st.markdown("<h1 style='text-align: center;'>Image Regeneration</h1>",unsafe_allow_html=True)

st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.sidebar.title("Style Transfer")

# displays a file uploader widget
image = st.sidebar.file_uploader("Choose an image",)

col1,col2,col3 = st.columns([1,1,2])


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# displays the select widget for the styles
style = st.sidebar.selectbox("Select your style",[i for i in STYLES.keys()])

if image is not None:
	with col1:
	    st.image(image)
    
    with col2:
        st.image(STYLES[style])

    with col3:
    # displays a button
        if st.sidebar.button("Style Transfer"):
            if image is not None and style is not None:
                with st.spinner('Applying Magic'):
                    style_image = generate_style(style,image)
                st.image(style_image)
            
            print(type(style_image))

            img = Image.fromarray(np.uint8(style_image*255))
            img.save("image.jpg")
            image_path = "image.jpg"

            # result.save("generated.jpg")

col1,col2,col3 = st.columns(3)
with col2:
    with open("image.jpg", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="image.jpg",
                mime="image/jpg"
        )

        
        

    





