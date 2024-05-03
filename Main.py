from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf
import cv2 as opencv
import os
import imghdr




AllowedExtension = ['jpg', 'jpeg', 'bmp', 'png']
ImagePath = "Data"
for dir in os.listdir(ImagePath):
    for images in os.listdir(os.path.join(ImagePath ,dir)):
        Image = os.path.join(ImagePath, dir, images)
        try: 
            img = opencv.imread(Image)
            cash = img
            tip = imghdr.what(Image)
            if tip not in AllowedExtension:
                os.remove(Image)
                print("We just deleted a image with extension: ".format(Image))
        except Exception as e: 
            print(e)


tf.data.Dataset

data = tf.keras.utils.image_dataset_from_directory(ImagePath)
dataITR = data.as_numpy_iterator()
