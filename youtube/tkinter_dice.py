import tkinter as gui
import random


def roll_die():
    lbl_value["text"] = random.randint(1, 6)


window = gui.Tk()
window.title("Rolling a Die 🙂")

window.rowconfigure([0, 1], minsize=100, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn_roll = gui.Button(master=window,
                      text="Roll", bg="yellow", fg="black",
                      relief=gui.RAISED,
                      command=lambda: roll_die())
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_value = gui.Label(master=window, text="1")
lbl_value.grid(row=1, column=0, sticky="nsew")

window.mainloop()