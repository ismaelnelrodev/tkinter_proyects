import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Bloc Nota Tkinter")
root.geometry("600x400")

menu_bar =tk.Menu()
root.config(menu=menu_bar)

#Variables
file_path =""

#Functions
def openAbout():
    messagebox.showinfo("BlockTkinter", "Version 1")


def newFile():
    text_field.delete("1.0",tk.END)

def openNewFile():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text File", "*.txt"),
            ("Python File", "*.py"),
            ("All File","*.*")
        ],
        defaultextension=".txt")
    
    with open(file_path, "r",encoding="utf-8") as file:
        text_field.delete("1.0",tk.END)
        text_field.insert(tk.INSERT, file.read())


def saveFile():
    global file_path
    if file_path:
        with open(file_path, "w",encoding="utf-8") as file:
            file.write(text_field.get("1.0",tk.END))

def saveFileAs():

    new_file_path = filedialog.asksaveasfilename(
        filetypes=[
            ("Text File", "*.txt"),
            ("Python File", "*.py"),
            ("All File","*.*")
        ],
        defaultextension=".txt")
    
    if new_file_path:
        with open(new_file_path, "w", encoding="utf-8") as file:
            file.write(text_field.get("1.0",tk.END))
        messagebox.showinfo("Save","Great News")
    
    newFile()


def copyText():
    text_field.event_generate(("<<Copy>>"))

def pasteText():
    text_field.event_generate(("<<Paste>>"))

def cutText():
    text_field.event_generate(("<<Cut>>"))


#Menu
bloc_menu =tk.Menu(menu_bar)
file_menu = tk.Menu(menu_bar)
edit_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="BlocTK", menu=bloc_menu)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

bloc_menu.add_command(label="About", command= openAbout)

file_menu.add_command(label="New", command= newFile)
file_menu.add_command(label="Open File", command= openNewFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_command(label="Save as", command= saveFileAs)

edit_menu.add_command(label="Copy", command= copyText)
edit_menu.add_command(label="Paste", command= pasteText)
edit_menu.add_command(label="Cut", command= cutText)


#Field Text
text_field= tk.Text(root)
text_field.pack(expand=True, fill="both")


root.mainloop()