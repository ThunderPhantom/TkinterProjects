from tkinter import*
from read import readset
root = Tk()
def setprinter():
    global root
    root.withdraw()
    import YWSetprinter
    YWSetprinter.sets()

def rs1():
    l=readset('webdev1')
    print (l)
def rs2():
    l=readset('webdev2')
    print (l)
def rs3():
    l=readset('webdev3')
    print (l)
def rs4():
    l=readset('webdev4')
    print (l)
def rs5():
    l=readset('webdev5')
    print (l)
def rs6():
    l=readset('webdev6')
    print (l)
def rs7():
    l=readset('webdev7')
    print (l)


def WebDev():
    global root
    root.deiconify()
    root.title("Web Development Sets")
    root.geometry('1000x850')
    Label(root, text = 'Choose a set', font = "Verdana 24 bold").grid(row = 0, column = 0, sticky = 'e')
    Button(root, text = 'Set 1', font = "Verdana 24",height = 3, command = rs1).grid(row = 1, column = 0, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Set 2', font = "Verdana 24", height = 3, command = rs2).grid(row = 2, column = 0, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Set 3', font = "Verdana 24", height = 3, command = rs3).grid(row = 3, column = 0, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Set 4', font = "Verdana 24", width = 20, height = 3, command = rs4).grid(row = 1, column = 1, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Set 5', font = "Verdana 24", width = 20, height = 3, command = rs5).grid(row = 2, column = 1, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Set 6', font = "Verdana 24", width = 20, height = 3, command = rs6).grid(row = 3, column = 1, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Set 7', font = "Verdana 24", width = 20, height = 3, command = rs7).grid(row = 4, column = 1, sticky = 'e'+'w', padx = 2)

    Button(root, text = 'Back', font = "Verdana 24", command = setprinter, width = 20, height = 3).grid(row = 5, column = 1, sticky = 'e'+'w', padx = 2)
