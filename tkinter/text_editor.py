"""Tutorial source: https://realpython.com/python-gui-tkinter/"""
import tkinter as gui
from tkinter.filedialog import askopenfilename, asksaveasfilename


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
    lbl_char_count["text"] = f"Characters:\n ", str(len(text_box.get("1.0", "end-1c")))


window = gui.Tk()
window.title("Text Editor")
window.iconbitmap("yawdie_code_logo.ico")
window.configure(bg='#404d44')
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

fr_buttons = gui.Frame(master=window, bg='#404d44')
btn_open = gui.Button(master=fr_buttons, text="OPEN",
                      width=10, bg='#e6f0e9', command=open_file)
btn_save = gui.Button(master=fr_buttons, text="SAVE AS",
                      width=10, bg='#e6f0e9', command=save_file)
lbl_char_count = gui.Label(master=fr_buttons, text="Characters: ")
btn_open.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="nsew", padx=5, pady=10)
lbl_char_count.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")

text_box = gui.Text(master=window, bg='#e6f0e9')
text_box.grid(row=0, column=1, sticky="nsew")

text_box.bind("<KeyPress>", count)
text_box.bind("<KeyRelease>", count)
window.mainloop()
