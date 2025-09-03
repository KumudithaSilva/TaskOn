import os
import pygame
from abc import ABC, abstractmethod


class IAudioService(ABC):
    """
    Abstract base class for audio playback services.
    """

    @abstractmethod
    def play(self, path: str):
        """
        Play an audio file.

        Args:
            path: Path to the audio file to play.
        """
        pass


class PygameAudionService(IAudioService):
    """
    Audio service implementation using pygame for playback.

    Attributes:
        base_path: Absolute directory where audio files are stored.
    """

    def __init__(self, base_path=None):
        """
        Initialize the Pygame audio service.

        Args:
            base_path: Directory path to load audio files from. If None,
                       defaults to '../assets/audio/' relative to this file.
        """
        if base_path is None:
            base_path = os.path.join(os.path.dirname(__file__), "../assets/audio")
        self.base_path = os.path.abspath(base_path)

        pygame.init()
        pygame.mixer.init()

    # --------------------------
    # Audio Loading / Playback
    # --------------------------

    def load_audio(self, filename: str):
        """
        Return the full path of an audio file if it exists.

        Args:
            filename: Name of the audio file.

        Returns:
            str: Full path to the audio file.

        Raises:
            FileNotFoundError: If the audio file does not exist.
        """
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Audio file not found: {path}")
        return path

    def play(self, filename: str):
        """
        Load and play an audio file using pygame.

        Args:
            filename: Name of the audio file to play.
        """
        path = self.load_audio(filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
