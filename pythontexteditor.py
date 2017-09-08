from tkinter import *
from tkinter import filedialog

def save_as():
    global text_box

    text_box_contents = text_box.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename(initialdir="/", filetypes=[("all files", "*.*")], title="Select file")

    try:
        file = open(save_location, "w+")
        file.write(text_box_contents)
        file.close()
    except:
        print("exception while saving file")

def save():
    global text_box

    text_box_contents = text_box.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename(initialdir="/", filetypes=[("all files", "*.*")], title="Select file")

    try:
        file = open(save_location, "w+")
        file.write(text_box_contents)
        file.close()
    except:
        print("exception while saving file")

tkinter = Tk("Text Editor")

text_box = Text(tkinter)

text_box.grid()

save_as_button = Button(tkinter, text="Save As", command=save_as)
save_button = Button(tkinter, text="Save", command=save)

save_as_button.grid()
save_button.grid()

tkinter.mainloop()
