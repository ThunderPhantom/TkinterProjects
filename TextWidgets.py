from tkinter import*

root = Tk()
root.geometry('640x480')
t = Text(root, height = 2, width = 30)
t.pack()
t.insert(END, 'Just a text widget \nin two lines \n')
