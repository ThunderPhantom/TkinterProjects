from tkinter import*
root = Tk()
root.title("My Test Program")
root.geometry("600x400")
mycolor = "blue"
label = Label(root, text='I am a label widget')
label1 = Label(root, text="Blue", bg = mycolor, fg = "black")
label1.pack(fill = X)
label2 = Label(root, text="red", bg = "red", fg = "white")
label2.pack(side = LEFT)
label3 = Label(root, text="green", bg = "green", fg = "white")
label3.pack(side = LEFT)
button = Button(root, text='I am a button')
label.pack()
button.pack()
frame1 = tkinter.Frame(root)
root.mainloop()