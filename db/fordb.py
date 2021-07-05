from tkinter import*
import tkinter as tk
import tkinter.messagebox
import datas

class FORDB:
	def __init__(self, root):
		self.root = root
		self.root.title("forlearndb")
		self.root.attributes("-fullscreen", True)

		self.root.config(bg="Antique white")

		itemID = StringVar()
		itemNAME = StringVar()
		itemPRICE = StringVar()


		def adddata():
			if(len(itemID.get()) != 0):
				datas.additem(itemID.get(), itemNAME.get(), itemPRICE.get())
				itemList.delete(0,END)
				itemList.insert(END, (itemID.get(), itemNAME.get(), itemPRICE.get()))

			self.txtiID.delete(0,END)
			self.txtiNAME.delete(0,END)
			self.txtiPRICE.delete(0,END)
		def ItemRec(event):
			global sd
			searchItd = itemList.curselection()[0]
			sd = itemList.get(searchItd)

			self.txtiID.delete(0,END)
			self.txtiID.insert(END,sd[1])
			self.txtiNAME.delete(0,END)
			self.txtiNAME.insert(END,sd[1])
			self.txtiPRICE.delete(0,END)
			self.txtiPRICE.insert(END,sd[1])

		mainframe = Frame(self.root, bg="cadet blue")
		mainframe.pack(expand = 1,fill = tk.BOTH,anchor = tk.NW)

		titframe = Frame(mainframe, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
		titframe.pack(side=TOP,expand = 1,fill = tk.BOTH,anchor = tk.NW)

		buttonframe = Frame(mainframe,bd=1,  bg="Ghost White", relief=RIDGE)
		buttonframe.pack(side=BOTTOM,expand = 1,fill = tk.BOTH,anchor = tk.NW)


		dataframe = Frame(mainframe, bd=1, relief=RIDGE, bg="cadet blue")
		dataframe.pack(side=BOTTOM,expand = 1,fill = tk.BOTH,anchor = tk.NW)

		


		self.titlbl = Label(titframe, font=('arial', 47, 'bold'), text="insert items", bg="Ghost White")
		self.titlbl.grid()

		self.lbliID = Label(dataframe, font=('arial', 20, 'bold'), text="Item ID", padx=2, pady=2, bg="Ghost White")
		self.lbliID.grid(row=0, column=0, sticky=W )
		self.txtiID = Entry(dataframe, font=('arial', 20, 'bold'), textvariable=itemID, width=40)
		self.txtiID.grid(row=0, column=1)

		self.lbliNAME = Label(dataframe, font=('arial', 20, 'bold'), text="Item Name", padx=2, pady=2, bg="Ghost White")
		self.lbliNAME.grid(row=1, column=0, sticky=W )
		self.txtiNAME = Entry(dataframe, font=('arial', 20, 'bold'), textvariable=itemNAME, width=40)
		self.txtiNAME.grid(row=1, column=1)

		self.lbliPRICE = Label(dataframe, font=('arial', 20, 'bold'), text="Item Price", padx=2, pady=2, bg="Ghost White")
		self.lbliPRICE.grid(row=2, column=0, sticky=W )
		self.txtiPRICE = Entry(dataframe, font=('arial', 20, 'bold'), textvariable=itemPRICE, width=40)
		self.txtiPRICE.grid(row=2, column=1)


		itemList = Listbox(dataframe, width=41, height=16, font=('arial', 12, 'bold'))
		itemList.bind('<<ListboxSelect>>', ItemRec)
		#itemList.grid(row=0, column=0, padx=8)


		self.btnAddData = Button(buttonframe, text='Add new', font=('arial', 12, 'bold'), height=1, width=10, bd=3, command=adddata)
		self.btnAddData.pack(fill = tk.BOTH
			)



if __name__ == '__main__':
	root = Tk()
	application = FORDB(root)
	root.mainloop()