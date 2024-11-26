import tkinter as tk
root = tk.Tk()
root.title("Simple Tkinter GUI")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked"))
button.pack()
root.mainloop()
