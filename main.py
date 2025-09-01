from tkinter import Tk
from app import TaskOnApp
from resources import ResourceLoader
from audio_service import PygameAudionService



def main():
    root = Tk()
    root.title("TaskOn")
    root.geometry("250x350")
    root.config(padx=5, pady=5, bg="#fdfdfd")
    root.resizable(False, False)
    root.iconbitmap("images/growing-seed.ico")

    loader = ResourceLoader()
    images = {
        "moon": loader.load_image("clock-green.png"),
        "oak": loader.load_image("growing-seed.png"),
        "play": loader.load_image("play.png"),
        "pause": loader.load_image("pause.png"),
        "checkbox": loader.load_image("checkbox.png"),
        "work": loader.load_image("studying.png"),
        "short_break": loader.load_image("short_break.png"),
        "long_break": loader.load_image("long_break.png"),
    }

    audio = PygameAudionService()
    TaskOnApp(root, images, audio)

    root.mainloop()



if __name__ == "__main__":
    main()


