import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

class SegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Image Segmentation")
        
        # Initialize state variables
        self.image = None
        self.original = None
        self.mask = None
        self.rect_start = None
        self.rect_end = None
        self.drawing = False
        
        # Create the interface
        self.setup_ui()
        
        # Initialize the GrabCut algorithm state
        self.bgd_model = np.zeros((1,65), np.float64)
        self.fgd_model = np.zeros((1,65), np.float64)
        
    def setup_ui(self):
        """Create the user interface components"""
        # Main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas for image display
        self.canvas = tk.Canvas(self.frame, cursor="cross")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Control panel
        self.control_panel = tk.Frame(self.frame)
        self.control_panel.pack(side=tk.RIGHT, padx=5, pady=5)
        
        # Buttons
        tk.Button(self.control_panel, text="Load Image", 
                 command=self.load_image).pack(pady=5)
        tk.Button(self.control_panel, text="Segment", 
                 command=self.perform_segmentation).pack(pady=5)
        tk.Button(self.control_panel, text="Reset", 
                 command=self.reset).pack(pady=5)
        tk.Button(self.control_panel, text="Save Result", 
                 command=self.save_result).pack(pady=5)
        
        # Canvas event bindings
        self.canvas.bind("<ButtonPress-1>", self.start_rect)
        self.canvas.bind("<B1-Motion>", self.draw_rect)
        self.canvas.bind("<ButtonRelease-1>", self.end_rect)
        
    def load_image(self):
        """Load an image file and prepare it for segmentation"""
        file_path = filedialog.askopenfilename()
        if file_path:
            # Load and resize image if necessary
            self.original = cv2.imread(file_path)
            height, width = self.original.shape[:2]
            
            # Resize if image is too large
            max_size = 800
            if max(height, width) > max_size:
                scale = max_size / max(height, width)
                new_width = int(width * scale)
                new_height = int(height * scale)
                self.original = cv2.resize(self.original, 
                                        (new_width, new_height))
            
            self.image = self.original.copy()
            self.mask = np.zeros(self.image.shape[:2], np.uint8)
            self.display_image()
            
    def display_image(self):
        """Update the canvas with the current image"""
        if self.image is not None:
            # Convert BGR to RGB for display
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(
                image=Image.fromarray(image_rgb)
            )
            
            # Update canvas
            self.canvas.config(
                width=self.image.shape[1],
                height=self.image.shape[0]
            )
            self.canvas.create_image(0, 0, anchor=tk.NW, 
                                   image=self.photo)
            
    def start_rect(self, event):
        """Begin drawing the rectangle"""
        self.rect_start = (event.x, event.y)
        self.drawing = True
        
    def draw_rect(self, event):
        """Update the rectangle as user drags the mouse"""
        if self.drawing and self.image is not None:
            # Remove previous rectangle
            self.canvas.delete("rect")
            
            # Draw new rectangle
            self.rect_end = (event.x, event.y)
            self.canvas.create_rectangle(
                self.rect_start[0], self.rect_start[1],
                self.rect_end[0], self.rect_end[1],
                outline="green", width=2, tags="rect"
            )
            
    def end_rect(self, event):
        """Finish drawing the rectangle"""
        self.drawing = False
        self.rect_end = (event.x, event.y)
        
    def perform_segmentation(self):
        """Execute the GrabCut algorithm"""
        if self.rect_start and self.rect_end and self.image is not None:
            # Create rectangle for GrabCut
            x1 = min(self.rect_start[0], self.rect_end[0])
            y1 = min(self.rect_start[1], self.rect_end[1])
            x2 = max(self.rect_start[0], self.rect_end[0])
            y2 = max(self.rect_start[1], self.rect_end[1])
            
            # Initialize mask and rectangle
            self.mask = np.zeros(self.image.shape[:2], np.uint8)
            rect = (x1, y1, x2-x1, y2-y1)
            
            # Perform GrabCut segmentation
            cv2.grabCut(self.image, self.mask, rect, 
                       self.bgd_model, self.fgd_model, 
                       5, cv2.GC_INIT_WITH_RECT)
            
            # Create mask for display
            mask2 = np.where(
                (self.mask==2) | (self.mask==0), 0, 1
            ).astype('uint8')
            
            # Apply mask to image
            self.image = self.original.copy()
            self.image = self.image * mask2[:,:,np.newaxis]
            
            # Update display
            self.display_image()
            
    def reset(self):
        """Reset the segmentation"""
        if self.original is not None:
            self.image = self.original.copy()
            self.mask = np.zeros(self.image.shape[:2], np.uint8)
            self.rect_start = None
            self.rect_end = None
            self.canvas.delete("rect")
            self.display_image()
            
    def save_result(self):
        """Save the segmented image"""
        if self.image is not None:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png"
            )
            if file_path:
                cv2.imwrite(file_path, self.image)

def main():
    root = tk.Tk()
    app = SegmentationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()