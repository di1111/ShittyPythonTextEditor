from tkinter import *
from tkinter import filedialog


def save_as(*_):
    global text_box, has_saved, save_location

    text_box_contents = text_box.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename(filetypes=[("all files", "*.*")], title="Save As...")

    try:
        file = open(save_location, "w+")
        file.write(text_box_contents)
        file.close()
        if not has_saved:
            has_saved = True

    except IOError:
        print("exception while saving file | io error")
    except BlockingIOError:
        print("exception while saving file | blocking io")
    except FileExistsError:
        print("exception while saving file | file exists")


def save(*_):
    global text_box, has_saved, save_location

    if not has_saved:
        save_as('blah')
    elif has_saved:
        text_box_contents = text_box.get("1.0", "end-1c")
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
    else:
        print("Unknown error has occurred while attempting to save file | unknown")


def open_file(*_):
    global has_saved, save_location

    if does_textbox_contain_text(text_box):
        print('Text box already has text in it, aborting open file')
    else:
        save_location = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

        file = open(save_location, "r+")
        text_box_contents = file.read()
        text_box.insert(END, text_box_contents)
        file.close()
    # Errors:
    # FileNotFoundError
    # IOError:
    # BlockingIOError
    # FileExistsError


def does_textbox_contain_text(textbox):
    text_box_contents = textbox.get("1.0", "end-1c")
    if text_box_contents:
        return True
    else:
        return False
