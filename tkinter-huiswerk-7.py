from tkinter import *
from tkinter import ttk

GEO = "450x400"
LIJST_ZICHTBAAR = 0
root = Tk()
root.geometry(GEO)
root.resizable(False, False)
root.title("huiswerk 6")

toplabel = Label(root, text="Kies eerst uw ziekte dan de dokter")
toplabel.grid(column=0, row=0)

dokters_ziektes = Label(root, text="door u gekozen:")
dokters_ziektes.grid(column=2, row=2)

druk_op = StringVar()
druk_af = StringVar()
dokter_ziektes = StringVar()

Radiobutton(root, text="database", variable=druk_op, value="database").grid(column=0, row=1)
Radiobutton(root, text="bestand", variable=druk_op, value="bestand").grid(column=1, row=1)
Radiobutton(root, text="textveld", variable=druk_op, value="textveld").grid(column=2, row=1)
Radiobutton(root, text="specialist", variable=druk_af, value="specialist").grid(column=0, row=2)
Radiobutton(root, text="ziektebeeld", variable=druk_af, value="ziektebeeld").grid(column=1, row=2)

def items_selected(event):
    selected_indices = lbo_dokters.curselection()
    selected_dokters = ",".join([lbo_dokters.get(i) for i in selected_indices])
    selected_index = lbo_ziek_ziektes.curselection()[0]
    selected_ziekte = ziek_ziektes[selected_index]
    dokter_ziektes.set(f"door u gekozen:\n\nDokters: {selected_dokters}\nZiekte: {selected_ziekte}")
    dokters_ziektes.config(textvariable=dokter_ziektes)

dokters = ["leo bonne",
            "johan boeket",
            "joris slist",
            "dirk ereyhers",
            "jef van de broek"]

i = 0
lbo_dokters = Listbox(root, exportselection=0)
lbo_dokters.bind("<<ListboxSelect>>", items_selected)

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

lbo_ziek_ziektes = Listbox(root, exportselection=0,
                      listvariable=string_ziek_ziektes,
                      height=LIJST_ZICHTBAAR,
                      selectmode="extended")
lbo_ziek_ziektes.grid(column=0, row=4, padx=10, pady=10)
lbo_dokters.grid(column=1, row=4, padx=10, pady=10)

root.mainloop()