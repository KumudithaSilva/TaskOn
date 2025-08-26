import os
from tkinter import PhotoImage

class ResourceLoader:
    def __init__(self, base_path=None):
        self.base_path = base_path or os.path.join(os.path.dirname(__file__), "images")

    def load_image(self, filename: str):
        path = os.path.join(self.base_path, filename)
        return PhotoImage(file=path) if os.path.exists(path) else None
