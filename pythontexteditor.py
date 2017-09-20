from tkinter import *

import fileoperations

def does_nothing(*_):
    pass


def quit_editor(*_):
    if fileoperations.does_textbox_contain_text(text_box):
        fileoperations.save()
    else:
        tkinter.quit()


tkinter = Tk("Text Editor")

text_box = Text(tkinter)

text_box.pack(fill=BOTH, expand=YES)

fileoperations.first_call(text_box)

menubar = Menu(tkinter)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=fileoperations.open_file)
filemenu.add_command(label="Save", command=fileoperations.save)
filemenu.add_command(label="Save As", command=fileoperations.save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit_editor)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=does_nothing)
editmenu.add_command(label="Copy", command=does_nothing)
editmenu.add_command(label="Paste", command=does_nothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=does_nothing)
menubar.add_cascade(label="Help", menu=helpmenu)

tkinter.bind("<Shift-Control-s>", fileoperations.save_as)
tkinter.bind("<Control-s>", fileoperations.save)
tkinter.bind("<Control-o>", fileoperations.open_file)
tkinter.config(menu=menubar)
tkinter.mainloop()
