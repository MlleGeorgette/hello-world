"""Tutorial source: https://realpython.com/python-gui-tkinter/"""
import re
import tkinter as gui
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random


# Functions
def open_file():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    text_box.delete("1.0", gui.END)
    with open(file_path, "r") as input_file:
        text = input_file.read()
        text_box.insert(gui.END, text)
    window.title(f"Text Editor - {file_path}")


def save_file():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = text_box.get("1.0", gui.END)
        output_file.write(text)
    window.title(f"Text Editor - {file_path}")


def count(event):
    words = text_box.get("1.0", "end-1c")
    w_count = len(re.findall('\w+', words))
    lbl_word_count["text"] = "Word count:\n " + str(w_count)
    lbl_char_count["text"] = "Characters:\n " + str(len(words))


def change_font():
    font_list = ["Helvetica 12 bold", "Verdana 20", "Cambria 8 bold"]
    font = random.choice(font_list)
    text_box['font'] = f"{font}"
    lbl_font['text'] = f"Font:\n " + str(font)


window = gui.Tk()
window.title("Text Editor")
window.configure(bg='#404d44')
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

fr_buttons = gui.Frame(master=window, bg='#404d44')
btn_open = gui.Button(master=fr_buttons, text="OPEN",
                      width=10, bg='#91a18d', command=open_file)
btn_save = gui.Button(master=fr_buttons, text="SAVE AS",
                      width=10, bg='#91a18d', command=save_file)
lbl_word_count = gui.Label(master=fr_buttons, text="Words:\n0 ")
lbl_char_count = gui.Label(master=fr_buttons, text="Characters:\n0 ")
lbl_font = gui.Label(master=fr_buttons, text="Font:\nArial 12 ")
btn_font = gui.Button(master=fr_buttons, text="CHANGE FONT",
                      width=10, bg='#91a18d', command=change_font)

# Add buttons and labels to frame1; add frame1 to window
btn_open.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="nsew", padx=5, pady=10)
lbl_word_count.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
lbl_char_count.grid(row=8, column=0, sticky="nsew", padx=5, pady=5)
lbl_font.grid(row=10, column=0, sticky="nsew", padx=5, pady=5)
btn_font.grid(row=12, column=0, sticky="nsew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")

text_box = gui.Text(master=window, font="Arial 12", bg='#e6f0e9')
text_box.grid(row=0, column=1, sticky="nsew")

text_box.bind("<KeyPress>", count)
text_box.bind("<KeyRelease>", count)
window.mainloop()
