from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.file_name = None
        self.text_widget = Text(self.master)
        self.text_widget.pack(fill=BOTH, expand=True)
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menubar, tearoff=False)
        edit_menu.add_command(label="Copy", command=self.copy)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        help_menu = Menu(menubar, tearoff=False)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def new_file(self):
        self.text_widget.delete(1.0, END)
        self.file_name = None

    def save_file(self):
        if self.file_name:
            with open(self.file_name, "w") as f:
                f.write(self.text_widget.get(1.0, END))
        else:
            self.file_name = filedialog.asksaveasfilename(defaultextension=".txt",
                                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if self.file_name:
                with open(self.file_name, "w") as f:
                    f.write(self.text_widget.get(1.0, END))

    def copy(self):
        self.text_widget.event_generate("<<Copy>>")

    def show_about(self):
        messagebox.showinfo("About Text Editor", "A simple text editor created using Tkinter")

root = Tk()
text_editor = TextEditor(root)
root.mainloop()