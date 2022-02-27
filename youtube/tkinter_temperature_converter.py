"""Tutorial source: https://realpython.com/python-gui-tkinter/"""
import tkinter as gui


def convert():
    value = entry_fahrenheit.get()
    celsius = (float(value) - 32) * (5/9)
    lbl_celsius["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


window = gui.Tk()
window.title("Temperature Converter")

window.resizable(width=False, height=False)
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=100, weight=1)

frame1 = gui.Frame()
lbl_about = gui.Label(master=frame1,
                      text="This app converts temperature from Fahrenheit to Celsius")
lbl_about.grid(row=0, column=0, sticky="nsew")
frame1.grid(row=0, column=0)

frame2 = gui.Frame()
lbl_fahrenheit = gui.Label(master=frame2, text="\N{DEGREE FAHRENHEIT}")
lbl_fahrenheit.grid(row=0, column=0, sticky="w")

entry_fahrenheit = gui.Entry(master=frame2, width=10)
entry_fahrenheit.grid(row=0, column=1, sticky="w")

btn_convert = gui.Button(master=frame2, text="Convert", width=10,
                         command=lambda: convert())
btn_convert.grid(row=0, column=2, sticky="e")

lbl_celsius = gui.Label(master=frame2, text="\N{DEGREE CELSIUS}")
lbl_celsius.grid(row=0, column=3, sticky="e")

frame2.grid(row=1, column=0, padx=5, pady=5)

window.mainloop()
