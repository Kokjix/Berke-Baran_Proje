#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

print(cv2.__version__)

cascade_src = 'cars.xml'
video_src = 'dataset/video1.avi'
#video_src = 'dataset/video2.avi'

src = cv2.imread(video_src)


cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

cimg = src.copy()



while True:
    

cv2.destroyAllWindows()
cap.release()