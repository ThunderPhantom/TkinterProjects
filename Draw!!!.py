from tkinter import*
root = Tk()
canvas_width = 500
canvas_height = 150
root.geometry('640x480')
w = Canvas(root, width = 200, height = 100)
w.pack()
def paint(event):
    global w
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill = python_green)
root.title('Painting using Ovals')
w.pack(expand = YES, fill = BOTH)
w.bind("<B1-Motion>", paint)
message = Label(root, text = "Press and Drag the mouse to draw.")
message.pack(side = BOTTOM)
mainloop()
