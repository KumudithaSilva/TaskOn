import os
import pygame
from abc import ABC, abstractmethod

class IAudioService(ABC):
    @abstractmethod
    def play(self, path:str):
        """Play an audio file."""
        pass

class PygameAudionService(IAudioService):
    def __init__(self, base_path="audio/"):
        self.base_path = base_path
        pygame.init()
        pygame.mixer.init()

    def load_audio(self, filename: str):
        """Return the full path of the audio file if it exists."""
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Audio file not found: {path}")
        return path

    def play(self, filename: str):
        """Load and play an audio file."""
        path = self.load_audio(filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()