from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import tkinter.font as tkFont


#**** Window Settings ****
root = Tk()
root.title("justapad")
root.iconbitmap("icon.ico")

#**** Functions ****
def new(event=""):
    if len(text_area.get("1.0", END+"-1c")) != 0:
        if messagebox.askyesno("Save?", "Do you wish to save?"):
            if save():
                text_area.delete(1.0, END)
        else:
            text_area.delete(1.0, END)

def open(event=""):
    if len(text_area.get("1.0", END+"-1c")) != 0:
        if messagebox.askyesno("Save?", "Do you wish to save?"):
            save()
        file = askopenfile()
        if file != None:
            text_area.delete(1.0, END)
            content = file.read()
            text_area.insert(1.0, content)
            file.close()
    else:
        file = askopenfile()
        if file != None:
            content = file.read()
            text_area.insert(1.0, content)
            file.close()

def save(event=""):
    saved = False
    list_of_filetypes = [("Text Documents", "*.txt"), ("All Files", "*.*")]
    file = asksaveasfile(filetypes=list_of_filetypes, defaultextension=list_of_filetypes)
    if file != None:
        text = text_area.get(1.0, END+"-1c")
        file.write(text)
        file.close()
        saved = True
    return saved

def exit():
    if len(text_area.get("1.0", END+"-1c")) != 0:
        if messagebox.askyesno("Save?", "Do you wish to save?"):
            save()
    root.quit()

def about():
    description = messagebox.showinfo("About justapad", "justapad\nv1.4\nA text editor made by Shubham Parihar.")

def undo(event=""):
    if len(text_area.get("1.0", END + "-1c")) != 0:
        text_area.edit_undo()

def redo(event=""):
    try:
        text_area.edit_redo()
    except:
        pass
def cut():
    text_area.focus_get().event_generate('<<Cut>>')

def copy():
    text_area.focus_get().event_generate('<<Copy>>')

def paste():
    text_area.focus_get().event_generate('<<Paste>>')

def increase_font_size():
    if custom_font['size'] < 100:
        custom_font['size'] += 1

def decrease_font_size():
    if custom_font['size'] > 4:
        custom_font['size'] -= 1

def togle_font(event):
    if event.keysym == 'plus':
        if custom_font['size'] < 100:
            custom_font['size'] += 1
    elif event.keysym == 'minus':
        if custom_font['size'] > 4:
            custom_font['size'] -= 1

#**** Scroll Bar ****
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

#**** Text Area ****
custom_font = tkFont.Font(family="Consolas", size=12)
text_area = Text(root, yscrollcommand=scrollbar.set, height=500, width=500, undo=TRUE)
text_area.configure(font=custom_font)
text_area.pack()
scrollbar.config(command=text_area.yview)

#**** Menu Bar ****
menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar, tearoff=0)
edit = Menu(menubar, tearoff=0)
format = Menu(menubar, tearoff=0)
help = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file)
file.add_command(label="New                             Ctrl+N", command=new)
file.add_command(label="Open...                        Ctrl+O", command=open)
file.add_command(label="Save                             Ctrl+S", command=save)
file.add_separator()
file.add_command(label="Exit", command=exit)

menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo                         Ctrl+Z", command=undo)
edit.add_command(label="Redo                          Ctrl+Y", command=redo)
edit.add_separator()
edit.add_command(label="Cut                             Ctrl+X", command=cut)
edit.add_command(label="Copy                          Ctrl+C", command=copy)
edit.add_command(label="Paste                          Ctrl+V", command=paste)

menubar.add_cascade(label="Format", menu=format)
format.add_command(label="Increase Font Size", command=increase_font_size)
format.add_command(label="Decrease Font Size", command=decrease_font_size)

menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About justapad", command=about)

#**** Shortcut Keys ****
root.bind('<Control-n>', new)
root.bind('<Control-o>', open)
root.bind('<Control-s>', save)
root.bind('<Control-z>', undo)
root.bind('<Control-y>', redo)
root.bind('<Control-plus>', togle_font)
root.bind('<Control-minus>', togle_font)

#**** Main Loop ****
root.geometry("500x500+450+150")
text_area.focus()
root.protocol('WM_DELETE_WINDOW', exit)
root.mainloop()