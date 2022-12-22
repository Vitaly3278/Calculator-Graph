import re
from tkinter import *


def click_button(data):
    if '=' in display.get():
        if re.fullmatch('[\+\-\*\/]', str(data)):
            last_value = display.get().split('= ')[1]
            clear()
            display.insert(0, last_value)
        else:
            clear()
    display.insert(100, data)


def click_count():
    if '=' not in display.get():
        display.insert(100, f' = {eval(display.get())}')


def clear():
    display.delete(0, END)


window = Tk()
window.title('Calculator')
frame = Frame(master=window, bg="lightgray", padx=10, pady=10)
frame.pack()

display = Entry(master=frame, fg="white", bg="black", width=30, borderwidth=10)
display.grid(row=0, column=0, columnspan=3)

button_clear = Button(master=frame, padx=10, pady=6, text="clear", width=5, height=1, bg="blue", fg="yellow",
                      command=clear)
button_clear.grid(row=0, column=3, pady=2)

button_1 = Button(master=frame, text="1", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(1))
button_1.grid(row=3, column=0)
button_2 = Button(master=frame, text="2", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(2))
button_2.grid(row=3, column=1)
button_3 = Button(master=frame, text="3", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(3))
button_3.grid(row=3, column=2)
button_4 = Button(master=frame, text="4", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(4))
button_4.grid(row=2, column=0)
button_5 = Button(master=frame, text="5", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(5))
button_5.grid(row=2, column=1)
button_6 = Button(master=frame, text="6", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(6))
button_6.grid(row=2, column=2)
button_7 = Button(master=frame, text="7", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(7))
button_7.grid(row=1, column=0)
button_8 = Button(master=frame, text="8", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(8))
button_8.grid(row=1, column=1)
button_9 = Button(master=frame, text="9", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(9))
button_9.grid(row=1, column=2)
button_0 = Button(master=frame, text="0", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(0))
button_0.grid(row=4, column=0)

button_dot = Button(master=frame, text=".", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                    command=lambda: click_button('.'))
button_dot.grid(row=4, column=1)
button_sum = Button(master=frame, text="+", padx=10, pady=10, width=5, height=2, bg="blue", fg="yellow",
                    command=lambda: click_button('+'))
button_sum.grid(row=4, column=3)
button_sub = Button(master=frame, text="-", padx=10, pady=10, width=5, height=2, bg="blue", fg="yellow",
                    command=lambda: click_button('-'))
button_sub.grid(row=3, column=3)
button_mul = Button(master=frame, text="*", padx=10, pady=10, width=5, height=2, bg="blue", fg="yellow",
                    command=lambda: click_button('*'))
button_mul.grid(row=2, column=3)
button_div = Button(master=frame, text="/", padx=10, pady=10, width=5, height=2, bg="blue", fg="yellow",
                    command=lambda: click_button('/'))
button_div.grid(row=1, column=3)
button_equal = Button(master=frame, text="=", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                      command=lambda: click_count())
button_equal.grid(row=4, column=2)

window.mainloop()