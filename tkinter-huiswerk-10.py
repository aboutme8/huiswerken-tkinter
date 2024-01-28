import tkinter as tk

def toevoegen_aan_lijst():
    invoer_text = invoerveld.get()
    if invoer_text:
        lijstbox.insert(tk.END, invoer_text)
        invoerveld.delete(0, tk.END)  # Wis de inhoud van het invoerveld

# Maak het hoofdvenster
root = tk.Tk()
root.title("Tkinter Uitgebreid Voorbeeld")

# Voeg een label toe aan het venster
label = tk.Label(root, text="Voer tekst in en klik op 'Toevoegen' om toe te voegen aan de lijst.")
label.pack(pady=10)

# Voeg een invoerveld toe aan het venster
invoerveld = tk.Entry(root, width=40)
invoerveld.pack(pady=10)

# Voeg een knop toe aan het venster
toevoeg_knop = tk.Button(root, text="Toevoegen", command=toevoegen_aan_lijst)
toevoeg_knop.pack(pady=10)

# Voeg een lijstbox toe aan het venster
lijstbox = tk.Listbox(root, width=40, height=10)
lijstbox.pack(pady=10)

# Start de GUI-loop
root.mainloop()