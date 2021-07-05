from tkinter import*
import tkinter as tk
import tkinter.messagebox
import datas

class forscreen():

	def __init__(self, root):
		self.root = root
		self.root.title("main gamen")
		self.root.attributes("-fullscreen", True)
		self.root.config(bg="White")

		itemID = StringVar()
		itemNAME = StringVar()
		itemPRICE = StringVar()

		def display():
			itemlist.delete(0,END)
			for row in datas.displayitem(itemID.get(), itemNAME.get(), itemPRICE.get()):
				itemlist.insert(END,row,str(""))

		def ItemRec(event):
			global sd
			searchItem = itemlist.curselection()[0]
			sd = itemlist.get(searchItem)

			self.txtID.delete(0,END)
			self.txtID.insert(END,sd[1])
			self.txtNAME.delete(0,END)
			self.txtNAME.insert(END,sd[2])
			self.txtPRICE.delete(0,END)
			self.txtPRICE.insert(END,sd[3])


		# def display():
		# 	itemlist.delete(0,END)
		# 	for row in datas.displayitem(itemID.get(), itemNAME.get(), itemPRICE.get()):
		# 		itemlist.insert(END,row,str(""))


		mainframe = Frame(self.root, bg="cadet blue")
		mainframe.grid()

		titframe = Frame(mainframe, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
		titframe.pack(side=TOP)

		buttonframe = Frame(mainframe,bd=1,  bg="Ghost White", relief=RIDGE)
		buttonframe.pack(side=BOTTOM)


		dataframe = Frame(mainframe, bd=1, relief=RIDGE, bg="cadet blue")
		dataframe.pack(side=BOTTOM)

		


		self.titlbl = Label(titframe, font=('arial', 47, 'bold'), text="Search items", bg="Ghost White")
		self.titlbl.grid()

		self.lblID = Label(dataframe, font=('arial', 20, 'bold'), text="Item ID", padx=2, pady=2, bg="Ghost White")
		self.lblID.grid(row=0, column=0, sticky=W )
		self.txtID = Entry(dataframe, font=('arial', 20, 'bold'), textvariable=itemID, width=40)
		self.txtID.grid(row=0, column=1)

		self.lblNAME = Label(dataframe, font=('arial', 20, 'bold'), text="Item Name", padx=2, pady=2, bg="Ghost White")
		self.lblNAME.grid(row=1, column=0, sticky=W )
		self.txtNAME = Entry(dataframe, font=('arial', 20, 'bold'), textvariable=itemNAME, width=40)
		self.txtNAME.grid(row=1, column=1)

		self.lblPRICE = Label(dataframe, font=('arial', 20, 'bold'), text="Item Price", padx=2, pady=2, bg="Ghost White")
		self.lblPRICE.grid(row=2, column=0, sticky=W )
		self.txtPRICE = Entry(dataframe, font=('arial', 20, 'bold'), textvariable=itemPRICE, width=40)
		self.txtPRICE.grid(row=2, column=1)


		itemlist = Listbox(dataframe, width=41, height=16, font=('arial', 12, 'bold'))
		itemlist.bind('<<ListboxSelect>>', ItemRec)
		#itemList.grid(row=0, column=0, padx=8)


		self.btnAddData = Button(buttonframe, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=3, command=display)
		self.btnAddData.grid(row=0, column=0)





if __name__ == '__main__':
	root = Tk()
	application = forscreen(root)
	root.mainloop()
