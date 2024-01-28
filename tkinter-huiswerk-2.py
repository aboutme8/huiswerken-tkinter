from tkinter import *

root = Tk()
root.geometry("312x324")
root.title("calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar()
input_frame = Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=("arial", 18, "bold"), textvariable=input_text, width=50, bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btn_frame = Frame(root, width=312, height=272.2, bg="grey")
btn_frame.pack()

# Buttons
buttons = [
    ("C", btn_clear, 0, 0),
    ("/", lambda: btn_click("/"), 0, 3),
    ("7", lambda: btn_click(7), 1, 0),
    ("8", lambda: btn_click(8), 1, 1),
    ("9", lambda: btn_click(9), 1, 2),
    ("*", lambda: btn_click("*"), 1, 3),
    ("4", lambda: btn_click(4), 2, 0),
    ("5", lambda: btn_click(5), 2, 1),
    ("6", lambda: btn_click(6), 2, 2),
    ("-", lambda: btn_click("-"), 2, 3),
    ("1", lambda: btn_click(1), 3, 0),
    ("2", lambda: btn_click(2), 3, 1),
    ("3", lambda: btn_click(3), 3, 2),
    ("+", lambda: btn_click("+"), 3, 3),
    ("0", lambda: btn_click(0), 4, 0),
    (".", lambda: btn_click("."), 4, 1),
    ("=", btn_equal, 4, 2),
]

for (text, command, row, column) in buttons:
    button = Button(btn_frame, text=text, fg="black", width=10, height=3, bd=0, command=command)
    button.grid(row=row, column=column, padx=1, pady=1)

root.mainloop()