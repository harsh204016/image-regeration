import os
import numpy as np 
import pandas as pd 
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import matplotlib.image as mpimg

from io import BytesIO
import base64


STYLES = {
    "style1": "style1.jpeg",
    "style2": "style2.jpeg",
    "style3": "style3.jpeg",
    "style4": "style4.jpeg",
    
}
path = "styles/"

def generate_style(style,image):
    if image:
        content_image_path = image
    else:
        raise Exception("Image not uploaded")
    
    style_image_path = path+STYLES[style]
    content_image = plt.imread(content_image_path,0)
    style_image = plt.imread(style_image_path)

    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = tf.image.resize(style_image, (256, 256))
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    
    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]
    tf.keras.preprocessing.image.save_img('./file.png',stylized_image[0])
    img = mpimg.imread('./file.png')
    
    return img


def get_image_download_link(img): 
    """
    Generates a link allowing the PIL image to be downloaded
    in:  PIL image
    out: href string
    """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}">Download Image</a>'
    return href

# # Create a folder for the TF hub module.
# $ mkdir /tmp/moduleA
# # Download the module, and uncompress it to the destination folder. You might want to do this manually.
# $ curl -L "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2?tf-hub-format=compressed" | tar -zxvC /tmp/moduleA
# # Test to make sure it works.
# $ python
# > import tensorflow_hub as hub
# > hub.Module("/tmp/moduleA")

    


