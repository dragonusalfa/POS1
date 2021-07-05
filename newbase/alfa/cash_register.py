from tkinter import*
import tkinter.messagebox

class Display:

	def __init__(self, rst):
		self.rst = rst
		self.rst.title("lets ")
		self.rst.attributes('-fullscreen', True)
		self.fullScreenState = False
		self.rst.bind("<F11>", self.gofull)
		self.rst.bind("<Escape>", self.quitfull)

# ====FRAME========FRAME========FRAME========FRAME========FRAME========FRAME========FRAME====
		MainFrame = Frame(self.rst, bg="gray")
		MainFrame.grid()

		TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
		TitleFrame.pack(side=TOP)
# ====LABELS========LABELS========LABELS========LABELS========LABELS========LABELS========LABELS====
		self.lblTit = Label(TitleFrame, font=('arial', 47, 'bold'), text="Cash register System", bg="Ghost White")
		self.lblTit.grid()


	def gofull(self, event):
		self.fullScreenState = not self.fullScreenState
		self.rst.attributes("-fullscreen", self.fullScreenState)


	def quitfull(self, event):
		self.fullScreenState=False
		self.rst.attributes("-fullscreen", self.fullScreenState)



if __name__=='__main__':
	rst = Tk()
	application = Display(rst)
	rst.mainloop()