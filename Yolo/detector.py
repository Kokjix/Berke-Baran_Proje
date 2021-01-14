import time
import sys
import torch as T
import numpy as np
import cv2
from utils import *
from darknet import *

class Detector:
	def __init__(self):
		self.yolo = Darknet("config.cfg","weights/yolov3.weights")
		self.CUDA = T.cuda.is_available()
		self.num_classes = 80
		self.classes = load_classes("data/coco.names")
		self.colors = create_colors(self.num_classes)
		self.in_dim = 416
		self.valid_classes = [2, 5, 7]

		if self.CUDA:
			self.yolo.cuda()

		self.yolo.eval()
		self.recentCoordinates = list()
		
	def detect(self, frame):
		img = prep_image(frame.copy() ,self.in_dim)

		if self.CUDA:
			img = img.cuda()

		result = self.yolo(img, self.CUDA)
		result = adjust_results(result, 0.5, self.num_classes)

		try:
			self.recentCoordinates = write_result(result.clone(), frame, self.in_dim, 
				self.classes, self.colors, self.valid_classes)
		except:
			return

		return result


if __name__ == "__main__":
	cap = cv2.VideoCapture("video.mp4")
	d = Detector()
	
	while True:
		ret, frame = cap.read()

		if not ret:
			break
		
		print(len(d.recentCoordinates))

		d.detect(frame)
		
		cv2.imshow("frame", frame)
		cv2.waitKey(1)
	