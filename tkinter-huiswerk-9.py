import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("RGB-slider")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

def get_current_value(value):
    value = int(float(value))
    return value

def update_slider1_value(value):
    value_label1.configure(text=get_current_value(value))
    update_color()

def update_slider2_value(value):
    value_label2.configure(text=get_current_value(value))
    update_color()
    
def update_slider3_value(value):
    value_label3.configure(text=get_current_value(value))
    update_color()

def update_color():
    r = slider1_value.get()
    g = slider2_value.get()
    b = slider3_value.get()
    color_hex = f"#{int(r):02x}{int(g):02x}{int(b):02x}"
    color_box.config(bg=color_hex)
    color_code.config(text=color_hex)

slider1_value = tk.DoubleVar()
slider1_label = ttk.Label(root, text="R:")
slider1_label.grid(column=0, row=0, sticky="w")
slider1 = ttk.Scale(root, from_=0, to=255, orient="horizontal", command=update_slider1_value, variable=slider1_value)
slider1.grid(column=1, row=1, sticky="we")
current_value_label1 = ttk.Label(root, text="0")
current_value_label1.grid(column=0, row=2, sticky="e", padx=(10, 0))
value_label1 = ttk.Label(root, text="0")
value_label1.grid(column=1, row=2, sticky="w")

slider2_value = tk.DoubleVar()
slider2_label = ttk.Label(root, text="G:")
slider2_label.grid(column=0, row=3, sticky="w")
slider2 = ttk.Scale(root, from_=0, to=255, orient="horizontal", command=update_slider2_value, variable=slider2_value)
slider2.grid(column=1, row=4, sticky="we")
current_value_label2 = ttk.Label(root, text="0")
current_value_label2.grid(column=0, row=5, sticky="e", padx=(10, 0))
value_label2 = ttk.Label(root, text="0")
value_label2.grid(column=1, row=5, sticky="w")

slider3_value = tk.DoubleVar()
slider3_label = ttk.Label(root, text="B:")
slider3_label.grid(column=0, row=6, sticky="w")
slider3 = ttk.Scale(root, from_=0, to=255, orient="horizontal", command=update_slider3_value, variable=slider3_value)
slider3.grid(column=1, row=7, sticky="we")
current_value_label3 = ttk.Label(root, text="0")
current_value_label3.grid(column=0, row=8, sticky="e", padx=(10, 0))
value_label3 = ttk.Label(root, text="0")
value_label3.grid(column=1, row=8, sticky="w")

color_box = tk.Label(root, text="", width=20, height=5)
color_box.grid(column=2, row=2, rowspan=4, padx=(10, 0))

color_code = ttk.Label(root, text="#000000")
color_code.grid(column=2, row=6, pady=(0, 10))

root.mainloop()