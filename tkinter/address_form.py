"""Tutorial source: https://realpython.com/python-gui-tkinter/"""
import tkinter as gui

window = gui.Tk()
window.title("Address Entry Form")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)


# Function to retrieve input
def retrieve_input():
    raw_data = entry_name.get()
    print(raw_data)


# Create 3 frames - instructions, form, buttons
label_instructions = gui.Label(text="Please complete the form.")
label_instructions.grid(row=0, column=5, sticky='w')

label_name = gui.Label(text="Name")
label_name.grid(row=1, column=0, sticky="w")
entry_name = gui.Entry(width=30)
entry_name.grid(row=1, column=1)

label_street = gui.Label(text="Street Name")
label_street.grid(row=2, column=0, sticky="w")
entry_street = gui.Entry(width=30)
entry_street.grid(row=2, column=1)

label_city = gui.Label(text="City")
label_city.grid(row=3, column=0, sticky="w")
entry_city = gui.Entry(width=30)
entry_city.grid(row=3, column=1)

label_postcode = gui.Label(text="Post Code")
label_postcode.grid(row=4, column=0, sticky="w")
entry_postcode = gui.Entry(width=30)
entry_postcode.grid(row=4, column=1)

label_country = gui.Label(text="Country")
label_country.grid(row=5, column=0, sticky="w")
entry_country = gui.Entry(width=30)
entry_country.grid(row=5, column=1)

button_submit = gui.Button(text="Submit",
                           fg="black", bg="grey", width=10, height=5,
                           command=lambda: retrieve_input())
button_submit.grid(row=6, column=2, sticky="e")

window.mainloop()