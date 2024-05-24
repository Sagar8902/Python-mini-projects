import cv2
import tkinter as tk
from tkinter import filedialog, Button, Label
from tkinter import ttk
from PIL import Image, ImageTk


def select_image():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename()
    if file_path:
        process_image(file_path)


def process_image(file_path):
    # Read and process the image
    image = cv2.imread(file_path)
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

    # Save the sketch
    output_path = "sketch.png"
    cv2.imwrite(output_path, sketch)

    # Display the sketch in the GUI
    display_image(output_path)


def display_image(image_path):
    # Load the image using PIL
    img = Image.open(image_path)
    img = img.resize((400, 400))  # Resize for display purposes
    img = ImageTk.PhotoImage(img)

    # Update the image label
    image_label.config(image=img)
    image_label.image = img


# Create the main window
root = tk.Tk()
root.title("Image to Sketch Converter")

# Create a frame for the buttons
frame = ttk.Frame(root)
frame.pack(pady=20)

# Add a button to select an image
select_button = Button(frame, text="Select Image", command=select_image)
select_button.pack(side=tk.LEFT, padx=10)

# Add a label to display the image
image_label = Label(root)
image_label.pack(pady=20)

# Run the GUI event loop
root.mainloop()
