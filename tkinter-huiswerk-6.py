from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

def screen_2():
    screen2 = Toplevel()
    screen2.title("derde scherm")
    screen2.geometry("400x300")

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT achter_naam FROM customers")
    rows = c.fetchall()
    achter_naam_list = [row[0] for row in rows]

    achter_naam_combobox = ttk.Combobox(screen2, values=achter_naam_list)
    achter_naam_combobox.pack()

    druk_button = Button(screen2, text="Ophalen", command=druk_data)
    druk_button.pack()

    voor_naam_textbox = Entry(screen2, textvariable=StringVar(value=""))
    voor_naam_textbox.pack()
    adres_textbox = Entry(screen2, textvariable=StringVar(value=""))
    adres_textbox.pack()
    woon_plaats_textbox = Entry(screen2, textvariable=StringVar(value=""))
    woon_plaats_textbox.pack()

    def druk_data():
        achter_naam = achter_naam_combobox.get()
        c.execute("SELECT * FROM customers WHERE achter_naam=?", (achter_naam,))
        customer = c.fetchone()
        if customer:
            voor_naam_textbox.insert(0, customer[1])
            adres_textbox.insert(0, customer[2])
            woon_plaats_textbox.insert(0, customer[3])

        c.close()
        conn.close()

root = Tk()
root.title("registreren")
root.geometry("400x300")

def login():
    screen1 = Toplevel()
    screen1.title("login")
    screen1.geometry("400x300")
    email_var = StringVar()
    password_var = StringVar()
    bal1 = Entry(screen1, bd=5, textvariable=email_var)
    bal1.grid(column=1, row=1)
    lab1 = Label(screen1, text="email")
    lab1.grid(column=0, row=1)
    bal2 = Entry(screen1, bd=5, textvariable=password_var, show="*")
    bal2.grid(column=1, row=2)
    lab2 = Label(screen1, text="pasword")
    lab2.grid(column=0, row=2)
    btn = Button(screen1, text="login", command=screen_2)
    btn.grid(column=1, row=5)

def registreren():
    email = balk1.get()
    controle_email = balk2.get()
    pasword = balk3.get()
    if email == controle_email:
        messagebox.showinfo("geregistreerd", "u bent geregistreerd, ga verder met login")
    else:
        messagebox.showinfo("error", "De emailadressen komen niet overeen.")

balk1 = Entry(root, bd=5)
balk1.grid(column=1, row=1)
balk2 = Entry(root, bd=5)
balk2.grid(column=1, row=2)
balk3 = Entry(root, bd=5, show="*")
balk3.grid(column=1, row=3)

label1 = Label(root, text="email")
label1.grid(column=0, row=1)
label2 = Label(root, text="controle email")
label2.grid(column=0, row=2)
label3 = Label(root, text="pasword")
label3.grid(column=0, row=3)

button1 = Button(root, text="registreren", command=registreren)
button1.grid(column=1, row=4)

button2 = Button(root, text="login", command=login)
button2.grid(column=2, row=4)

root.mainloop()
