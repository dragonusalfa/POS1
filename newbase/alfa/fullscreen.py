import tkinter as tk

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.bind("<F1>", self.geoscreen)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def geoscreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.window.geometry("600x600"))
        # self.geometry("600x600")/

if __name__ == '__main__':
    app = Fullscreen_Example()  