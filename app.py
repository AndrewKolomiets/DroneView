import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

class DroneViewApp:
	def __init__(self, root):
		self.root = root
		self.root.title("DroneViewApp")
		self.yoloModel = YOLO('settings\\visdrone.pt')
		self.setup_ui()
        
	def setup_ui(self):
		"""Create the user interface components"""
		# Main frame
		self.statusVar = tk.StringVar()
		self.statusVar.set("Ready")
		statusBar = tk.Label(self.root, textvariable=self.statusVar, relief=tk.SUNKEN, anchor="w")
		statusBar.pack(side=tk.BOTTOM, fill=tk.X)

		self.notebook = ttk.Notebook(self.root)
		self.notebook.pack(fill=tk.BOTH, expand=True)
		
		#initial frame
		self.initialFrame = tk.Frame(self.notebook)
#		self.initialFrame.pack(fill=tk.BOTH, expand=True)
		self.notebook.add(self.initialFrame, text = 'Initial')
		
        # Canvas for image display
		self.initialCanvas = tk.Canvas(self.initialFrame, cursor="cross")
		self.initialCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		
        # Control panel
		self.control_panel = tk.Frame(self.initialFrame, background='gray', width="40px")
		self.control_panel.pack(side=tk.BOTTOM, fill=tk.Y, expand=True)

		loadButton = tk.Button(self.control_panel, text="Load Image", command=self.load_source_file, width=10)
		loadButton.pack(pady=3, padx=3)


		#extract features
		self.extractFrame = tk.Frame(self.notebook)
		self.notebook.add(self.extractFrame, text = 'Extract')
		
        # Canvas for image display
		holder = tk.Frame(self.extractFrame)
		holder.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		
		self.extractCanvas = tk.Canvas(holder, cursor="cross")
		self.extractCanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		self.extractCanvas2 = tk.Canvas(holder, cursor="cross")
		self.extractCanvas2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		
        # Control panel
		self.control_panel = tk.Frame(self.extractFrame, background='gray', width="40px")
		self.control_panel.pack(side=tk.BOTTOM, fill=tk.Y, expand=True)

		extractButton = tk.Button(self.extractFrame, text="extractButton", command=self.extract_features, width=10)
		extractButton.pack(pady=3, padx=3)

	def load_source_file(self):
		self.sourceFilePath = filedialog.askopenfilename()

		if self.sourceFilePath:
			# Load and resize image if necessary
			self.sourceImage = cv2.imread(self.sourceFilePath)
			self.sourceImage = cv2.cvtColor(self.sourceImage, cv2.COLOR_BGR2RGB)
			self.sourceImageShape = self.sourceImage.shape[:2]
			print(self.sourceImageShape, max(self.sourceImageShape))
			
			self.statusVar.set(f"{self.sourceFilePath} {self.sourceImageShape[1]} x{self.sourceImageShape[0]}")
			self.display_image(self.sourceImage, self.initialCanvas, 1280)

	def display_image(self, inImage, inCanvas, max_size):
		"""Update the canvas with the current image"""
		scale = 1.0
		if inImage is not None:
			# Resize if image is too large
			if max_size!=0 and max(self.sourceImageShape) > max_size:
				scale = max_size / max(self.sourceImageShape)
				new_width = int(self.sourceImageShape[1] * scale)
				new_height = int(self.sourceImageShape[0] * scale)
				img = cv2.resize(inImage, (new_width, new_height))
			else:
				img = np.copy(inImage)

			inCanvas.photo = ImageTk.PhotoImage( image=Image.fromarray(img) )

			# Update canvas
			inCanvas.config( width=img.shape[1], height=img.shape[0] )
			inCanvas.imageScale=scale
			inCanvas.create_image(0, 0, anchor=tk.NW, image=inCanvas.photo)

	def extract_features(self):
			img = np.copy(self.sourceImage)
			self.yoloResults = self.yoloModel(self.sourceFilePath)
			
			for idx, box in enumerate(self.yoloResults[0].boxes):
				if self.yoloResults[0].names[box.cls.numpy()[0]] == 'car':
					bbox = box.xyxy[0].numpy(force=True).astype(int)
					pt1 = (bbox[0], bbox[1])
					pt2 = (bbox[2], bbox[3])
					cv2.rectangle(img, pt1, pt2, (255,0,0), 2)

			self.display_image(img, self.extractCanvas, 800)
			self.extractCanvas.bind("<Button-1>", self.feature_selected)

	def feature_selected(self, event):
		scale = self.extractCanvas.imageScale
		point = (event.x/scale, event.y/scale)
		self.currentSelectedIndex = self.pick_point(point)
		if self.currentSelectedIndex != -1:
			bbox = self.yoloResults[0].boxes[self.currentSelectedIndex].xyxy[0].numpy(force=True).astype(int)
			self.currentSelectedFrame = self.sourceImage[bbox[1]:bbox[3], bbox[0]:bbox[2]]
			self.display_image(self.currentSelectedFrame, self.extractCanvas2, 0)
			

	def pick_point(self,point):
		for idx, box in enumerate(self.yoloResults[0].boxes):
			if self.yoloResults[0].names[box.cls.numpy()[0]] == 'car':
				bbox = box.xyxy[0].numpy(force=True)
				if (point[0] > bbox[0] and point[0] < bbox[2]) and (point[1] > bbox[1] and point[1] < bbox[3]):
					return idx
		return -1
		
def main():
	root = tk.Tk()
	app = DroneViewApp(root)
	root.mainloop()

if __name__ == "__main__":
	main()
