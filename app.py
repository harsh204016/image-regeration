from fastapi import FastAPI,HTTPException,File,UploadFile
from pydantic import BaseModel
from typing import Optional , List


#image 
from PIL import Image
from src import inference
import config
import numpy as np
import uuid
import cv2





@app.post("/{style}")
def generate_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.STYLES[style]
    output, resized = inference.inference(model, image)
    name = f"/result/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)
    return {"name": name}


