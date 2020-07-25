from tkinter import *

font10 = "-family {Microsoft Sans Serif} -size 26 -weight bold" \
         " -slant roman -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 16 -weight normal -slant " \
         "roman -underline 0 -overstrike 0"
font13 = "-family {Segoe UI} -size 16 -weight bold -slant " \
         "roman -underline 0 -overstrike 0"

dic = {"activebackground": "#d9d9d9", "activeforeground": "#000000", "background": "#f0f0f0", "borderwidth": "0",
       "disabledforeground": "#a3a3a3", "font": font12, "foreground": "#000000", "highlightbackground": "#d9d9d9",
       "highlightcolor": "black", "pady": "0", }
dic2 = dic.copy()
dic2.update({"background": "#ffffff", "font": font13})


def root(x):
    return x ** 1 / 2


def cube(x):
    return x ** 1 / 9


def foo(str_):
    lis = {'M': '%', '3√': 'cube', '√': 'root', '²': '**2', 'x': '*'}
    for i in lis:
        str_ = lis[i].join(j for j in str_.split(i))
    return str_


class Calculator:
    def __init__(self, _root):
        self.root = _root
        self.main_var = StringVar()
        self.root.geometry("340x336+575+128")
        self.root.title("Calculator")
        self.root.configure(background="#d9d9d9")
        self.e = Entry(self.root, background="#e6e6e6", borderwidth="0", disabledforeground="#a3a3a3", font=font10,
                       foreground="#000000", insertbackground="black", justify=RIGHT, width=17,
                       textvariable=self.main_var)
        self.e.place(x=0, y=0, height=70)
        Button(self.root, text='''√''', width=63, command=lambda: self.btn_text("√", True, True), **dic)
        Button(self.root, text='''M''', width=63, command=lambda: self.btn_text("M", True), **dic)
        Button(self.root, text='''3√''', width=63, command=lambda: self.btn_text("3√", True, True), **dic)
        Button(self.root, text='''a²''', width=63, command=lambda: self.btn_text("²", True), **dic)
        Button(self.root, text='''CE''', width=63, command=self.clear, **dic)
        Button(self.root, text='''C''', width=63, command=lambda: self.clear_last(), **dic)
        Button(self.root, text='''(''', width=63, command=lambda: self.btn_text("("), **dic)
        Button(self.root, text='''+-''', width=63, command=lambda: self.adder(), **dic)
        Button(self.root, text=''')''', width=63, command=lambda: self.btn_text(")"), **dic)
        Button(self.root, text='''=''', width=63, command=lambda: self.result(), **dic)
        Button(self.root, text='''.''', width=63, command=lambda: self.btn_text("."), **dic)
        Button(self.root, text='''/''', width=63, command=lambda: self.btn_text("/"), **dic)
        Button(self.root, text='''+''', width=63, command=lambda: self.btn_text("+"), **dic)
        Button(self.root, text='''X''', width=63, command=lambda: self.btn_text("x"), **dic)
        Button(self.root, text='''-''', width=63, command=lambda: self.btn_text("-"), **dic)

        Button(self.root, text='''7''', command=lambda: self.btn_text("7"), **dic2)
        Button(self.root, text='''8''', command=lambda: self.btn_text("8"), **dic2)
        Button(self.root, text='''9''', command=lambda: self.btn_text("9"), **dic2)
        Button(self.root, text='''4''', command=lambda: self.btn_text("4"), **dic2)
        Button(self.root, text='''5''', command=lambda: self.btn_text("5"), **dic2)
        Button(self.root, text='''6''', command=lambda: self.btn_text("6"), **dic2)
        Button(self.root, text='''1''', command=lambda: self.btn_text("1"), **dic2)
        Button(self.root, text='''2''', command=lambda: self.btn_text("2"), **dic2)
        Button(self.root, text='''3''', command=lambda: self.btn_text("3"), **dic2)
        Button(self.root, text='''0''', command=lambda: self.btn_text("0"), **dic2)

        self.data = [(3, 70), (70, 70), (137, 70), (204, 70), (271, 70), (3, 123), (3, 176),
                     (3, 282), (3, 229), (70, 282), (204, 282), (271, 282), (271, 123), (271, 176),
                     (271, 229), (70, 123), (137, 123), (204, 123), (70, 176), (137, 176),
                     (204, 176), (70, 229), (137, 229), (204, 229), (137, 282)]
        self.place_elements()

    def clear(self):
        self.main_var.set("")

    def btn_text(self, txt, brac=False, front_cal=False):
        if front_cal:
            self.main_var.set(txt + '(' + self.main_var.get() + ')')
        elif brac:
            self.main_var.set('(' + self.main_var.get() + ')' + txt)
        else:
            self.main_var.set(self.main_var.get() + txt)

    def clear_last(self):
        self.main_var.set(self.main_var.get()[0:-1])

    def adder(self):
        if len(self.main_var.get()) != 0:
            if self.main_var.get()[0] == '-':
                self.main_var.set(self.main_var.get()[1:])
            else:
                self.main_var.set('-' + self.main_var.get())
        else:
            self.main_var.set('-')

    def result(self):
        if self.main_var.get() != '':
            try:
                self.main_var.set(eval(foo(self.main_var.get())))
            except:
                self.main_var.set("Invalid Input ")

    def place_elements(self):
        lis = self.root.winfo_children()[1:]
        for i in range(len(lis)):
            lis[i].place(x=self.data[i][0], y=self.data[i][1], height=50, width=63)


def main():
    window = Tk()
    window.resizable(0, 0)
    Calculator(window)
    window.mainloop()


if __name__ == '__main__':
    main()
