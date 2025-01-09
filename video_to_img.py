import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import os

class SegmentationApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Video to frames")
		
		self.fps = 30.0
		# Create the interface
		self.setup_ui()
        
	def setup_ui(self):
		"""Create the user interface components"""
		# Main frame
		self.frame = tk.Frame(self.root)
		self.frame.pack(fill=tk.BOTH, expand=True)
		
        # Canvas for image display
		self.canvas = tk.Canvas(self.frame, cursor="cross")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		
        # Control panel
		self.control_panel = tk.Frame(self.frame, background='gray', width="40px")
		self.control_panel.pack(side=tk.BOTTOM, fill=tk.Y, expand=True)

		fileInfoLabel = tk.Label(self.control_panel, text='FileInfo:', background='gray')
		fileInfoLabel.pack(padx=3, pady=0)

		self.fileinfoEntry = tk.Entry(self.control_panel, state=tk.DISABLED, background='gray')
		self.fileinfoEntry.pack(padx=3, pady=0, fill='x')

		self.fileinfoEntryStr = tk.StringVar()  
		self.fileinfoEntry["textvariable"] = self.fileinfoEntryStr

		loadButton = tk.Button(self.control_panel, text="Load Video", command=self.load_video, width=10)
		loadButton.pack(pady=3, padx=3)

		intervalLabel = tk.Label(self.control_panel, text='Capture interval(sec):', background='gray')
		intervalLabel.pack(padx=3, pady=0)

		self.outIntervalEntryVar = tk.DoubleVar()  
		self.outIntervalEntryVar.set("1.0")
		outIntervalSpin = tk.Spinbox(self.control_panel, from_=0.0, to=10.0, increment=0.05, textvariable=self.outIntervalEntryVar, background='gray')
		outIntervalSpin.pack(padx=3, pady=5)

		exportButton = tk.Button(self.control_panel, text="Export", command=self.perform_export, width=10)
		exportButton.pack(padx=3, pady=3)

		self.outProgress = ttk.Progressbar(self.control_panel, orient = 'horizontal')
		self.outProgress.pack(padx=3, pady=3, fill='x')

	def load_video(self):
		file_path = filedialog.askopenfilename()

		if file_path:
			# Load and resize image if necessary
			self.stream = cv2.VideoCapture(file_path)
   
			ret, self.currentFrame = self.stream.read()

			self.srcHeight, self.srcWidth = self.currentFrame.shape[:2]

			self.fps = self.stream.get(cv2.CAP_PROP_FPS)
			print(f"Width:{self.srcWidth} Height:{self.srcHeight} PFS:{self.fps}")
			
			self.fileinfoEntryStr.set(f"{self.srcWidth} x{self.srcHeight} {self.fps:,.1f} fps")
   
			self.display_image()

	def perform_export(self):
		framesTotal = self.stream.get(cv2.CAP_PROP_FRAME_COUNT)
		targetInterval = self.outIntervalEntryVar.get()
		frameTime = 1.0 / self.fps
		accumulator = 0.0
		print(frameTime)
		outDir = filedialog.askdirectory()

		frameCounter = 0
		currentFrame = 1
		self.outProgress['maximum'] = framesTotal
		
		while currentFrame != framesTotal:
#			self.outProgressEntryStr.set(f"{currentFrame} of {framesTotal}")
			self.outProgress.step()
			if accumulator == 0.0:
				fname = 'frame_' + str(frameCounter).zfill(3) + '.jpg'
				fpath = outDir + '/' + fname
				frameCounter = frameCounter+1
				print(f"store frame {currentFrame} as {fpath}")
				cv2.imwrite(fpath, self.currentFrame)
				#display keyframe
				self.display_image()

			ret, self.currentFrame = self.stream.read()

			currentFrame = currentFrame+1
			accumulator += frameTime
			if accumulator >= targetInterval:
				accumulator = 0.0
    
			self.root.update()

	def display_image(self):
		"""Update the canvas with the current image"""
		if self.currentFrame is not None:
			# Convert BGR to RGB for display
			img = np.copy(self.currentFrame)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			# Resize if image is too large
			max_size = 800
			if max(self.srcHeight, self.srcWidth) > max_size:
				scale = max_size / max(self.srcHeight, self.srcWidth)
				new_width = int(self.srcWidth * scale)
				new_height = int(self.srcHeight * scale)
				img = cv2.resize(img, (new_width, new_height))

			self.photo = ImageTk.PhotoImage( image=Image.fromarray(img) )

			# Update canvas
			self.canvas.config( width=img.shape[1], height=img.shape[0] )
			self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

def main():
	root = tk.Tk()
	app = SegmentationApp(root)
	root.mainloop()

if __name__ == "__main__":
	main()
