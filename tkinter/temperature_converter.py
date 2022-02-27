"""Tutorial source: https://realpython.com/python-gui-tkinter/"""
import tkinter as gui


def convert():
    value = entry_fahrenheit.get()
    celsius = (float(value) - 32) * (5/9)
    lbl_celsius["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


window = gui.Tk()
window.title("Temperature Converter")

window.resizable(width=False, height=False)
window.configure(bg="#272322")
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=100, weight=1)

frame1 = gui.Frame(bg="#272322")
lbl_about = gui.Label(master=frame1,
                      text="It's getting hot in here...",
                      font="Arial 12",  bg="#272322", fg="#D5664A")
lbl_about.grid(row=0, column=0, sticky="nsew")
frame1.grid(row=0, column=0)

frame2 = gui.Frame(bg="#272322")
lbl_fahrenheit = gui.Label(master=frame2, text="\N{DEGREE FAHRENHEIT}", bg="#272322", fg="white")
lbl_fahrenheit.grid(row=0, column=0, sticky="nsew")

entry_fahrenheit = gui.Entry(master=frame2, width=10, bg="#E9DAD6", fg="black")
entry_fahrenheit.grid(row=0, column=1, sticky="nsew")

btn_convert = gui.Button(master=frame2, text="Convert", font="Arial 12 bold", width=10,
                         bg="#E9DAD6", fg="#272322",
                         command=lambda: convert())
btn_convert.grid(row=0, column=2, sticky="nsew")

lbl_celsius = gui.Label(master=frame2, text="\N{DEGREE CELSIUS}", bg="#272322", fg="white")
lbl_celsius.grid(row=0, column=3, sticky="nsew")

frame2.grid(row=1, column=0, padx=5, pady=5)

window.mainloop()
