import os
import sys
from tkinter import PhotoImage


class ResourceLoader:
    """
    Load image resources for the application.

    Attributes:
        base_path: Absolute directory path where images are stored.
    """

    def __init__(self, base_path=None):
        """
        Initialize the ResourceLoader.

        Args:
            base_path: Directory path to load images from. If None, defaults
                       to 'assets/images' inside PyInstaller temp or source folder.
        """
        if base_path is None:
            if hasattr(sys, '_MEIPASS'):
                # Running inside PyInstaller bundle
                base_path = os.path.join(sys._MEIPASS, 'assets', 'images')
            else:
                # Running from source
                base_path = os.path.join(os.path.dirname(__file__), 'assets', 'images')
        self.base_path = os.path.abspath(base_path)

    # --------------------------
    # Resource Loading Methods
    # --------------------------

    def load_image(self, filename: str):
        """
        Load an image from the base path.

        Args:
            filename: Name of the image file.

        Returns:
            PhotoImage: Tkinter PhotoImage object if file exists, else None.
        """
        path = os.path.join(self.base_path, filename)
        return PhotoImage(file=path) if os.path.exists(path) else None

    def get_resource_path(self, filename: str) -> str:
        """
        Get the absolute file path for a resource file.

        Args:
            filename: Name of the resource file.

        Returns:
            Absolute path to the resource file.
        """
        return os.path.join(self.base_path, filename)