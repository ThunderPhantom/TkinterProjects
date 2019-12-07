from tkinter import*
master = Tk()
master.geometry('680x480')
w = Scale(master, from_=0, to = 420)
w.pack()
w = Scale(master, from_=0, to = 200, orient = HORIZONTAL)
w.pack()

mainloop()
