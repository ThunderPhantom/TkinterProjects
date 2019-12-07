from tkinter import*

root = Tk()
s = Scrollbar(root)
t = Text(root, height = 4,  width = 50)
s.pack(side = RIGHT, fill = Y)
t.pack(side = LEFT, fill = Y)
s.config(command = t.yview)
t.config(yscrollcommand = s.set)
quote = """blah blah blah blah blah blah blah blah blah blah blahblah blah blah blah blah blah blah blah blah blah blahblah blah blah blah blah blah blah blah blah blah blahblah blah blah blah blah blah blah blah blah blah blahblah blah blah blah blah blah blah blah blah blah blahblah blah blah blah blah blah blah blah blah blah blah"""
t.insert(END, quote)
mainloop()
