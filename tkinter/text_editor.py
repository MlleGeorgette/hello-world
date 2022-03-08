"""Tutorial source: https://realpython.com/python-gui-tkinter/"""
import tkinter as gui
from tkinter.filedialog import askopenfilename, asksaveasfilename


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


window = gui.Tk()
window.title("Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

fr_buttons = gui.Frame(window)
btn_open = gui.Button(master=fr_buttons, text="OPEN",
                      width=10, height=5,
                      command=open_file)
btn_save = gui.Button(master=fr_buttons, text="SAVE AS",
                      width=10, height=5,
                      command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")

text_box = gui.Text(master=window)
text_box.grid(row=0, column=1, sticky="nsew")

window.mainloop()
