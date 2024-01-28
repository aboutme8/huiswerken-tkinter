from tkinter import *
import sqlite3

def save_data():
    conn = sqlite3.connect('RegistratieAdressen.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS `adres`(
                  `idadres` INTEGER PRIMARY KEY AUTOINCREMENT,
                  `straatnaam` VARCHAR (45) NOT NULL,
                  `huisnummer` VARCHAR (45) NOT NULL,
                  `postcode` VARCHAR (45) NOT NULL,
                  `woonplaats` VARCHAR (45) NOT NULL,
                  `idpersoon` INTEGER NOT NULL)''')
    c.execute("INSERT INTO adres (straatnaam, huisnummer, postcode, woonplaats, idpersoon) VALUES (?,?,?,?,?)", 
              (straat_naam_entry.get(), huis_nummer_entry.get(), post_code_entry.get(), woon_plaats_entry.get(), 0))
    conn.commit()
    conn.close()

root = Tk()
root.title("RegistratieAdressen")

straat_naam_label = Label(root, text="straatnaam")
straat_naam_label.grid(row=0, column=0)

straat_naam_entry = Entry(root)
straat_naam_entry.grid(row=0, column=1)

huis_nummer_label = Label(root, text="huisnummer")
huis_nummer_label.grid(row=1, column=0)

huis_nummer_entry = Entry(root)
huis_nummer_entry.grid(row=1, column=1)

post_code_label = Label(root, text="postcode")
post_code_label.grid(row=2, column=0)

post_code_entry = Entry(root)
post_code_entry.grid(row=2, column=1)

woon_plaats_label = Label(root, text="woonplaats")
woon_plaats_label.grid(row=3, column=0)

woon_plaats_entry = Entry(root)
woon_plaats_entry.grid(row=3, column=1)

opslaan_button = Button(root, text="opslaan", command=save_data)
opslaan_button.grid(row=4, column=1)

root.mainloop() 