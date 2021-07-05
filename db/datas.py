import sqlite3


def totorial():
	con = sqlite3.connect("fordb.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, itemID text, itemNAME text, itemPRICE text)")
	con.commit()
	con.close()

def additem(itemID, itemNAME, itemPRICE):
	con=sqlite3.connect("fordb.db")
	cur=con.cursor()
	cur.execute("INSERT INTO items VALUES (NULL,?,?,?)",(itemID, itemNAME, itemPRICE))
	con.commit()
	con.close()

def displayitem(id, itemID="", itemNAME="", itemPRICE=""):
	con=sqlite3.connect("fordb.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM items WHERE itemID=? OR itemNAME=? OR itemPRICE=?", (itemID,itemNAME,itemPRICE))
	rows=cur.fetchall()
	con.close()
	return rows


totorial()


#ef studentData():
	# con=sqlite3.connect("student.db")
	# cur = con.cursor()
	# cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text,Surname text, DoB text,\
	# 			Age text, Gender text, Address text, Mobile text)")
	# con.commit()
	# con.close()