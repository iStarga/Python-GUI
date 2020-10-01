from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=60, borderwidth=2)
e.grid(row=0, column=0, columnspan=4)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def button_add():
    first = e.get()
    global f_num
    global math
    math = "+"
    f_num = int(first)
    e.delete(0, END)


def button_sub():
    first = e.get()
    global f_num
    global math
    math = "-"
    f_num = int(first)
    e.delete(0, END)


def button_div():
    first = e.get()
    global f_num
    global math
    math = "/"
    f_num = int(first)
    e.delete(0, END)


def button_equal():
    second = e.get()
    e.delete(0, END)
    if math == "+":
        e.insert(0, f_num + int(second))
    elif math == "-":
        e.insert(0, f_num - int(second))
    elif math == "/":
        e.insert(0, f_num / int(second))


Button(root, text="1", padx=40, pady=20,
       command=lambda: button_click(1)).grid(row=3, column=0)
Button(root, text="2", padx=40, pady=20,
       command=lambda: button_click(2)).grid(row=3, column=1)
Button(root, text="3", padx=40, pady=20,
       command=lambda: button_click(3)).grid(row=3, column=2)

Button(root, text="4", padx=40, pady=20,
       command=lambda: button_click(4)).grid(row=2, column=0)
Button(root, text="5", padx=40, pady=20,
       command=lambda: button_click(5)).grid(row=2, column=1)
Button(root, text="6", padx=40, pady=20,
       command=lambda: button_click(6)).grid(row=2, column=2)

Button(root, text="7", padx=40, pady=20,
       command=lambda: button_click(7)).grid(row=1, column=0)
Button(root, text="8", padx=40, pady=20,
       command=lambda: button_click(8)).grid(row=1, column=1)
Button(root, text="9", padx=40, pady=20,
       command=lambda: button_click(9)).grid(row=1, column=2)

Button(root, text="0", padx=40, pady=20,
       command=lambda: button_click(0)).grid(row=4, column=0)

Button(root, text="Clear", padx=77, pady=20, command=clear).grid(
    row=4, column=1, columnspan=2)


Button(root, text="+", padx=50, pady=20,
       command=button_add).grid(row=1, column=3)
Button(root, text="-", padx=51, pady=20,
       command=button_sub).grid(row=2, column=3)
Button(root, text="/", padx=50, pady=20,
       command=button_div).grid(row=3, column=3)


Button(root, text="=", padx=50, pady=20,
       command=button_equal).grid(row=4, column=3)


root.mainloop()
