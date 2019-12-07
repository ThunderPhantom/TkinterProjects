from tkinter import*
def read():
    ifile = open('LoginInformation.txt', 'r')
    for lines in ifile:
        username,password = lines.split()
        return username, password
root = Tk()
root.title("Login")
root.geometry("600x75")
e1 = StringVar()
e2 = StringVar()

def logincommand():
    user = e1.get()
    passw = e2.get()
    username, password = read()
    if username == user and password == passw:
        print('Access Granted')
        root.destroy()
        root.quit()
        import YWSetprinter
    else:
        print('Access Denied')
Label(root, text = 'Username:').grid(row = 0, column = 0, sticky = 'e')
Entry(root, width = 60, textvariable=e1).grid(row = 0, column = 1, padx = 2, pady = 2, sticky = 'we', columnspan = 9)
Label(root, text = 'Password:').grid(row = 1, column = 0, sticky = 'e')
Entry(root, width = 60, textvariable=e2, show = "*").grid(row = 1, column = 1, padx = 2, pady = 2, sticky = 'we', columnspan = 9)
Button(root, text = "Login", command = logincommand).grid(row = 2, column = 5, sticky = 'e'+'w', padx = 2)
