from tkinter import *
from tkinter.messagebox import showinfo

GEO = "450x400"
LIJST_ZICHTBAAR = 0

def items_selected(event):
    selected_indices = lbo_dokters.curselection()
    selected_dokters = ",".join([lbo_dokters.get(i) for i in selected_indices])
    selected_index = lbo_ziek_ziektes.curselection()[0]
    selected_ziekte = ziek_ziektes[selected_index]
    msg = f"You selected:\n\nDokters: {selected_dokters}\nZiekte: {selected_ziekte}"
    showinfo(title="Information", message=msg)

def screen_2():
    GEO = "450x400"
    LIJST_ZICHTBAAR = 0

    def items_selected(event):
        selected_indices = lbo_dokters.curselection()
        selected_dokters = ",".join([lbo_dokters.get(i) for i in selected_indices])
        selected_index = lbo_ziek_ziektes.curselection()[0]
        selected_ziekte = ziek_ziektes[selected_index]
        msg = f"You selected:\n\nDokters: {selected_dokters}\nZiekte: {selected_ziekte}"
        showinfo(title="Information", message=msg)

    dokters = ["leo bonne",
                "johan boeket",
                "joris slist",
                "dirk ereyhers",
                "jef van de broek"]

    screen2 = Toplevel(root)
    screen2.geometry(GEO)
    screen2.resizable(False, False)
    screen2.title("huiswerk 5")

    toplabel = Label(screen2, text="Kies eerst uw ziekte dan de dokter")
    toplabel.grid(column=0, row=0)

    lbo_dokters = Listbox(screen2, exportselection=0)
    lbo_dokters.bind("<<ListboxSelect>>", items_selected)

    i = 0
    for dokter in dokters:
        lbo_dokters.insert(i, dokter)
        i += 1
    
    i = 1
    ziek_ziektes = ["exzeem",
                    "reuma",
                    "hernia",
                    "oorontsteking",
                    "corona"]
    string_ziek_ziektes = StringVar(value=ziek_ziektes)

    lbo_ziek_ziektes = Listbox(screen2, exportselection=0,
                               listvariable=string_ziek_ziektes,
                               height=LIJST_ZICHTBAAR,
                               selectmode="extended")
    lbo_dokters.grid(column=0, row=1, padx=20, pady=20)
    lbo_ziek_ziektes.grid(column=1, row=1, padx=20, pady=20)

root = Tk()
root.geometry(GEO)
root.resizable(False, False)
root.title("huiswerk 6")

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
        showinfo("geregistreerd", "u bent geregistreerd, ga verder met login")
    else:
        showinfo("error", "De emailadressen komen niet overeen.")

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