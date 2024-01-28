from tkinter import *

root = Tk()
root.geometry("950x750")

frame = Frame(root, bd=4, bg="green")
frame.pack()

label = Label(frame, text="mijn eerste opdracht")
label.pack()

leftframe = Frame(root, bg="red", bd=8)
leftframe.pack(side=LEFT)  # Aangenomen dat je 'leftframe' aan de linkerkant wilt plaatsen

label1 = Label(leftframe, text="1")
label1.pack()

rightframe = Frame(root, bg="blue", bd=8)  # Hier kun je een andere kleur gebruiken voor 'rightframe'
rightframe.pack(side=RIGHT)

label2 = Label(rightframe, text="2")
label2.pack()

root.title("huiswerk 1 tkinter.")
root.mainloop()