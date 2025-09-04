import os
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
                       to '../assets/images/' relative to this file.
        """
        if base_path is None:
            # Absolute path relative to this file
            base_path = os.path.join(os.path.dirname(__file__), "assets/images")
        self.base_path = os.path.abspath(base_path)  # converts to absolute path

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