import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

class SingleImageViewer:
    def __init__(self, root):
        self.root = root
        self.image_path = None

        self.label = Label(root)
        self.label.pack(padx=10, pady=10)

        self.prev_button = Button(root, text="Previous", command=self.show_previous, state="disabled")
        self.prev_button.pack(side="left", padx=10, pady=10)

        self.next_button = Button(root, text="Next", command=self.show_next, state="disabled")
        self.next_button.pack(side="right", padx=10, pady=10)

        self.load_image()

    def load_image(self):
        if self.image_path:
            image = Image.open(self.image_path)
            resized_image = image.resize((400, 400), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(resized_image)
            self.label.config(image=photo)
            self.label.image = photo

            
            self.prev_button.config(state="normal")
            self.next_button.config(state="normal")
        else:
            self.label.config(text="No image loaded.")
            self.prev_button.config(state="disabled")
            self.next_button.config(state="disabled")

    def show_previous(self):
        
        pass

    def show_next(self):
        
        pass

    def open_file(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        self.load_image()

if __name__ == "__main__":
    root = Tk()
    root.title("Single Image Viewer")
    app = SingleImageViewer(root)

    
    button_open = Button(root, text="Open Image", command=app.open_file)
    button_open.pack(pady=10)

    root.mainloop()
