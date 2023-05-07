
from tkinter import *
def miles_to_km():
    a=float(input.get())
    b=a*1.609
    km_result_label.config(text=f"{b}")



window = Tk()
window.title("Miles to Kilometer")
window.config(padx=20, pady=20)


input = Entry(width=7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Kilometres")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()




'''
import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Miles to Kilometers Converter")
    window.geometry("375x200")


    miles = tk.Label(window, text="Enter Miles:")


    kilometres = tk.Label(window, text="Kilometers:")


    miles.place(x=50, y=30)



    input = tk.Entry(window, width=12)


    input.place(x=200, y=35)


    kilometres.place(x=50, y=100)


    space = tk.Label(window, text=" ")


    space.place(x=180, y=100)

    def button_click():
        kilometers = round(float(input.get()) * 1.60934, 5)
        space.configure(text=str(kilometers) + '  Kilometers')


    calculate_button = tk.Button(window, text="Click Me To Convert", command=button_click)

    calculate_button.place(x=90, y=150)
    window.mainloop()


main()

'''