from tkinter import *


def convert_mile_to_km(mile):
    return round(mile * 1.609, 2)


def on_calculate_button_click():
    kilometers_value.config(text=convert_mile_to_km(float(miles_input.get())))


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=10, pady=10, background="white")

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_text = Label(text="Miles")
miles_text.grid(row=0, column=2)

equals_text = Label(text="is equal to")
equals_text.grid(row=1, column=0)

kilometers_value = Label(text="0")
kilometers_value.grid(row=1, column=1)

kilometers_text = Label(text="Kilometers")
kilometers_text.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=on_calculate_button_click)
calc_button.grid(row=2, column=1)

window.mainloop()
