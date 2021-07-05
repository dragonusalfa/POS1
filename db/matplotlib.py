import tkinter as tk
import numpy as np
# from matplotlib import pyplot as plt
from PIL import Image as img

def cbPlot(evt):
    print('cbPlot')

def cbPaint(evt):
    print('cbPaint')

bTxtList = [('Plot',cbPlot),('Paint',cbPaint)] # 名前とコールバック関数のタプルで管理
eInitList = [0, 0, 0]

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.createWidgets(bTxtList, eInitList)

    def createWidgets(self, bTxtList, eInitList):
        for eInit in eInitList:
            e = tk.Entry()
            e.insert(tk.END, eInit)
            e.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)

        for bTxt in bTxtList:
            b = tk.Button(text = bTxt[0]) # [0] = 名称
            b.bind("<Button-1>", bTxt[1]) # [1] = コールバック関数
            b.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)

        canvas = tk.Canvas(self, bg = 'white')
        canvas.pack()


root = tk.Tk().title("Visualizer for function")
app = Application(master = root)
app.mainloop()