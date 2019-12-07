from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox

#**** Window Settings ****
root = Tk()
root.title("justapad")
root.iconbitmap("icon.ico")

#**** Functions ****
def new():
    if len(text_area.get("1.0", END+"-1c")) != 0:
        if messagebox.askyesno("Save?", "Do you wish to save?"):
            save()
            text_area.delete(1.0, END)
        else:
            text_area.delete(1.0, END)
def open():
    file = askopenfile()
    text_area.delete(1.0, END)
    if file != None:
        content = file.read()
        text_area.insert(1.0, content)
        file.close()

def save():
    list_of_filetypes = [("Text Documents", "*.txt"), ("All Files", "*.*")]
    file = asksaveasfile(filetypes=list_of_filetypes, defaultextension=list_of_filetypes)
    if file != None:
        text = text_area.get(1.0, END+"-1c")
        file.write(text)
        file.close()

def exit():
    root.quit()

def about():
    description = messagebox.showinfo("About justapad", "justapad\nv1.0\nMade by Shubham Parihar.")

def undo():
    if len(text_area.get("1.0", END + "-1c")) != 0:
        text_area.edit_undo()

def redo():
    try:
        text_area.edit_redo()
    except:
        pass

#**** Scroll Bar ****
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

#**** Text Area ****
text_area = Text(root, yscrollcommand=scrollbar.set, height=500, width=500, undo=TRUE)
text_area.pack()
scrollbar.config(command=text_area.yview)

#**** Menu Bar ****
menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar, tearoff=0)
edit = Menu(menubar, tearoff=0)
help = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new)
file.add_command(label="Open...", command=open)
file.add_command(label="Save", command=save)
file.add_separator()
file.add_command(label="Exit", command=exit)

menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo", command=undo)
edit.add_command(label="Redo", command=redo)

menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About justapad", command=about)

#**** Main Loop ****
root.geometry("500x500+450+150")
root.mainloop()