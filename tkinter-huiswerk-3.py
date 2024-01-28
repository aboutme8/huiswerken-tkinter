from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("inlog")
root.geometry("400x300")

balk1 = StringVar()
balk2 = StringVar()

def controleren():
    if balk1.get() == balk2.get():
        messagebox.showinfo("inlog", "Emails match")
        return True
    else:
        messagebox.showinfo("error", "Emails do not match")
        return False

def registreren():
    root2 = Tk()
    root2.title("registreren")
    root2.geometry("400x300")
    label = Label(root2, text="email").grid(column=0, row=1)
    entry = Entry(root2, bd=5, textvariable=balk1).grid(column=2, row=1)
    label2 = Label(root2, text="herhaling email").grid(column=0, row=3)
    entry2 = Entry(root2, bd=5, textvariable=balk2).grid(column=2, row=3)
    btn1 = Button(root2, text="registreren", command=controleren).grid(column=5, row=5)

email = Label(root, text="email").grid(column=0, row=1)
pasword = Label(root, text="pasword").grid(column=0, row=3)
mail = Entry(root, bd=5).grid(column=2, row=1)
pas = Entry(root, bd=5).grid(column=2, row=3)
btn = Button(root, text="registreren", command=registreren).grid(column=5, row=5)

root.mainloop()