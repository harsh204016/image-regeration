import streamlit as st
import numpy as np
import os

#image
from config import STYLES , generate_style 
from PIL import Image

st.markdown("<h1 style='text-align: center;'>Image Regeneration</h1>",unsafe_allow_html=True)
st.set_option("deprecation.showfileUploaderEncoding", False)

st.text("")
st.text("")

# defines an h1 header
st.sidebar.title("Style Transfer")

# displays a file uploader widget
image = st.sidebar.file_uploader("Choose an image",)

col1,col2,col3 = st.columns([1,1,2])

image_path = ""

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# displays the select widget for the styles
style = st.sidebar.selectbox("Select your style",[i for i in STYLES.keys()])

if image is not None:
	with col1:
	    st.image(image)
    
if image is not None:
    with col1:
        img = Image.open(os.path.abspath(os.getcwd())+"/styles/"+STYLES[style])
        st.image(img)

if st.sidebar.button("Style Transfer"):
    with col3:
        st.text("")
        st.text("")
    # displays a button
        if image is not None and style is not None:
            with st.spinner('Applying Magic'):
                style_image = generate_style(style,image)
            st.image(style_image)
        
        print(type(style_image))

        img = Image.fromarray(np.uint8(style_image*255))
        img.save("image.jpg")
        image_path = "image.jpg"

            # result.save("generated.jpg")

if image_path !="":
    col1,col2,col3 = st.columns(3)
    with col2:
        with open("image.jpg", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="image.jpg",
                    mime="image/jpg"
            )

        
        

    





