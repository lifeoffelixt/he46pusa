import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    X_new = Image.fromarray(X)
    try:
        X_new = X_new.resize(resize)
    except:
        raise Exception('The resize input must be a list or tuple')
    return X_new
