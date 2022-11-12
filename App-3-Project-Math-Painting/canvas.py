import numpy as np
from PIL import Image


class Canvas:
    """Object where all shapes are drawn on"""
    def __init__(self, height, weight, color):
        self.weight = weight
        self.height = height
        self.color = color
        # Create a 3D array of zeros
        self.data = np.zeros((self.height, self.weight, 3), dtype=np.uint8)
        # Change the [0, 0, 0] with color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current numpy array into image"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
