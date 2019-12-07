from tkinter import*
root = Tk()
root.title('Images')
root.geometry('640x480')
w = Canvas(root, width = 640, height = 480)
img = PhotoImage(file = "earth.gif")
w.create_image(0, 0, anchor = NW, image = img)
w.pack()
mainloop()
