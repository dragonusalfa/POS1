import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("syokudou")

root.geometry("1024x600")

frame1=tk.LabelFrame(root, width=700, height=500, text="メニュー")
frame1.place(x=0,y=0)

frame2=tk.LabelFrame(root, width=213, height=400, text="注文内容")
frame2.place(x=780,y=0)
frame2.propagate(0)

frame3=tk.LabelFrame(root,width=213, height=100, text="合計金額")
frame3.place(x=780,y=500)
frame3.propagate(0)


a_notebook = ttk.Notebook(frame1, width=760, height=400)
tab1 = ttk.Frame(a_notebook)


a_notebook.add(tab1, text = '麺類')

a_notebook.grid()

UDN_How    = 0
UDN_Var    = tk.StringVar(value="")

GOK = 0
GOK_Var = tk.StringVar(value="合計" + str(GOK) + "円")

def UDNcom():
    global UDN_How
    UDN_How = UDN_How + 1

    global GOK
    GOK = GOK + 200

    UDN_Var.set("うどん 200円" + str(UDN_How) + "個")
    GOK_Var.set("合計" + str(GOK) + "円")

UDN = tk.Button(tab1, width=18, height=5, command=UDNcom, text="うどん\n￥200")
UDN.grid(column=0, row=0)

UDN_Lab = tk.Label(frame2, textvariable=UDN_Var)
UDN_Lab.grid()

GOK_Lab = tk.Label(frame3, textvariable=GOK_Var)
GOK_Lab.grid()

root.mainloop()