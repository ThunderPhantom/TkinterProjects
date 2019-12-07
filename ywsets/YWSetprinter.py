from tkinter import*
root = Tk()
    
def callscratch():
    global root
    root.withdraw()
    import ScratchSets
    ScratchSets.Scratch()

def callpython():
    global root
    root.withdraw()
    import PythonSets
    PythonSets.Python()

def callpygame():
    global root
    root.withdraw()
    import PygameSets
    PygameSets.Pygame()

def callgpio():
    global root
    root.withdraw()
    import GPIOSets
    GPIOSets.GPIO()

def calltkinter():
    global root
    root.withdraw()
    import TkinterSets
    TkinterSets.Tkinter()

def callwebdev():
    global root
    root.withdraw()
    import WebDevSets
    WebDevSets.WebDev()

def sets():
    global root
    root.deiconify()
    root.title("YoungWonks Sets")
    root.geometry('1000x850')
    Label(root, text = 'Choose a section of sets', font = "Verdana 24 bold").grid(row = 0, column = 0, sticky = 'e')
    Button(root, text = 'Scratch', font = "Verdana 24",height = 3, command = callscratch).grid(row = 1, column = 0, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Python', font = "Verdana 24", height = 3, command = callpython).grid(row = 2, column = 0, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Pygame', font = "Verdana 24", height = 3, command = callpygame).grid(row = 3, column = 0, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'GPIO', font = "Verdana 24", width = 20, height = 3, command = callgpio).grid(row = 1, column = 1, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Tkinter', font = "Verdana 24", width = 20, height = 3, command = calltkinter).grid(row = 2, column = 1, sticky = 'e'+'w', padx = 2)
    Button(root, text = 'Web Development', font = "Verdana 24", width = 20, height = 3, command = callwebdev).grid(row = 3, column = 1, sticky = 'e'+'w', padx = 2)

sets()
