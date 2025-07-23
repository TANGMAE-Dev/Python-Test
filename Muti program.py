import tkinter as tk
from doctest import master

def show_output():
    number = str(number_input.get())

    output = ''
    for i in range(1,13):
        output += str(number) + ' X ' + str(i)
        output += '=' +str(number*i)+'\n'

    output_label = tk.Label(window, text=output)

window = tk.Tk()
window.title("Suit")
window.minsize(1920, 1080)

title_label = tk.Label(window, text="Suit")
title_label.pack()

number_input = tk.Entry(master=window)
number_input.pack()

go_button = tk.Button(
    master=window, text='go',
    command=show_output()
)
go_button.pack()

number_output = tk.Label(master=window)
number_output.pack()

window.mainloop()
