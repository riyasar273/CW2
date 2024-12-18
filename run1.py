import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def create_tiny_img(path):
    img = Image.open(path)
    height = img.height
    width = img.width
    cropped_img = img.crop(((width/2)-8,(height/2)-8 , (width/2)+8, (height/2)+8))
    return cropped_img

