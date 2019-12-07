from tkinter import*
root = Tk()
root.title("Farenheit to Celsius Converter")
root.geometry("600x75")
f = IntVar()

def convert():
    c = 0
    df = int(f.get())
    c = (5/9)*(df-32)
    print(c)
    Label(root, text = c).grid(row = 1, column = 2, sticky = 'e')
Label(root, text = 'Farenheit:').grid(row = 0, column = 0, sticky = 'e')
Entry(root, width = 25, textvariable = f).grid(row = 0, column = 1, padx = 2, pady = 2, sticky = 'we', columnspan = 9)
Label(root, text = 'Celsius').grid(row = 1, column = 0, sticky = 'e')
Button(root, text = "Convert", command = convert).grid(row = 2, column = 3, sticky = 'e')


    
