from turtle import shape
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt 
from PIL import Image

path = r'C:\Users\ASUS\Desktop\Sem 6th\CS encr project\Final\c.jpg'

my_img = cv2.imread(path)

print("Shape of my_img",my_img.shape)
print(my_img.shape[0])
smallest = my_img.min(axis=(0, 1))

largest = my_img.max(axis=(0, 1))

print("highest RGB value",largest)
print("minimum RGB value",smallest)

