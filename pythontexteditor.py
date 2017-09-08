from tkinter import *
from tkinter import filedialog


def save_as(none):
    global text_box

    text_box_contents = text_box.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename(initialdir="/", filetypes=[("all files", "*.*")], title="Select file")

    try:
        file = open(save_location, "w+")
        file.write(text_box_contents)
        file.close()
    except IOError:
        print("exception while saving file | io error")
    except BlockingIOError:
        print("exception while saving file | blocking io")
    except FileExistsError:
        print("exception while saving file | file exists")


tkinter = Tk("Text Editor")

text_box = Text(tkinter)

text_box.grid()

tkinter.bind("<Shift-Control-S>", save_as)
tkinter.mainloop()
