import sys
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLabel
import PyQt6.QtGui as QtGui


from PIL import Image
from ultralytics import YOLO

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#model = YOLO('visdrone.pt')
#model = YOLO('dota8-obb.pt')
#model = YOLO('yolov8n.pt')
#model = YOLO('yolov8s.pt')
#model = YOLO('yolov8n-seg.pt')
#model = YOLO('yolov8s-seg.pt')
#model = YOLO('yolov8n-obb.pt')
#model = YOLO('yolov8s-obb.pt')
#model = YOLO('yolov8n-pose.pt')
#model = YOLO('dotav1.5.pt')
#results = model("img\\cars-003.jpg")


# Define a main window class
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("PyQt6 Example")
		self.setGeometry(100, 100, 800, 600)

		self.imageFrame = QLabel(self)
		self.imageFrame.move(0,0)
		self.imageFrame.resize(300,300)
  
		# Add a label to the window
		self.label = QLabel("Hello from PyQt6!", self)
		self.label.resize(200,100)
		self.label.move(10, 10)
		self.label.setStyleSheet("font-size: 16px; font-weight: bold;")

		# Add a button to change the label text
		button = QPushButton("Test Yolo", self)
		button.move(150, 150)
		button.clicked.connect(self.testYoloClicked)

		button = QPushButton("Test", self)
		button.move(150, 350)
		button.clicked.connect(self.testClicked)

  
	def testYoloClicked(self):
		model = YOLO('visdrone.pt')
		self.label.setText("You clicked the button!")
		results = model("img\\cars-002.jpg")
		for r in results:
			img = r.plot()  # plot a BGR numpy array of predictions
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			#plt.imshow(img)
			#plt.show(), plt.draw()	
			img = QtGui.QImage(img, img.shape[1],img.shape[0], img.shape[1] * 3, QtGui.QImage.Format.Format_RGB888)
			pix = QtGui.QPixmap(img)
			self.imageFrame.setPixmap(pix)
   

	def testClicked(self):
		img = cv2.imread("img\\cars-002.jpg")
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		#plt.imshow(img)
		#plt.show(), plt.draw()
		img = QtGui.QImage(img, img.shape[1],img.shape[0], img.shape[1] * 3, QtGui.QImage.Format.Format_RGB888)
		pix = QtGui.QPixmap(img)
		self.imageFrame.setPixmap(pix)
    

# Main application execution
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())