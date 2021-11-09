import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    row = X.shape[0]
    col = X.shape[1]
    try:
        resized_image = [[ X[int(row * r / resize[0])][int(col * c / resize[1])]
                            for c in range(resize[1])] for r in range(resize[0])]
    except:
        raise Exception('The resize input must be a list or tuple')
    return resized_image
