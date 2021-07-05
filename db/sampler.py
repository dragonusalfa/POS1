from tkinter import*
import tkinter as tk
import tkinter.messagebox

class Sampler(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)
		self.pack(expand = 1,fill = tk.BOTH,anchor = tk.NW)
		self.master.attributes("-fullscreen", True)


root = tk.Tk().title("Sampler")
app = Sampler(master = root)
app.mainloop()