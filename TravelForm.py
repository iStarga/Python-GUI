from tkinter import *

root = Tk()


def check():
    if (name.get() != "") and (phone.get() != "") and (gender.get() != "") and (em_contact.get() != "") and (
            payment_mode.get() != ""):
        return True
    return False


def submit():
    if check():
        with open("Travel.dat", 'a') as f:
            query = '{' + f'\n\t"name":{name.get()}\n\t"phone":{phone.get()}\n\t"gender":{gender.get()}\n\t"em_contact":{em_contact.get()}\n\t' \
                          f'"payment_mode":{payment_mode.get()}\n\t"Meal":{mealOnTheWay.get()}\n' + '}\n'
            f.write(query)
            confirm['text'] = "Booking Confirmed"
    else:
        confirm['text'] = "Please Fill The Form Correct"


root.geometry("444x264")
root.resizable(0, 0)
Label(root, text="Welcome to Awesome Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

Label(root, text="Name").grid(row=1, column=2)
Label(root, text="Phone No.").grid(row=2, column=2)
Label(root, text="Gender").grid(row=3, column=2)
Label(root, text="Emergency Contact").grid(row=4, column=2)
Label(root, text="Payment Mode").grid(row=5, column=2)

name = StringVar()
phone = StringVar()
gender = StringVar()
em_contact = StringVar()
payment_mode = StringVar()
mealOnTheWay = IntVar()

Entry(root, textvariable=name).grid(row=1, column=3)
Entry(root, textvariable=phone).grid(row=2, column=3)
Entry(root, textvariable=gender).grid(row=3, column=3)
Entry(root, textvariable=em_contact).grid(row=4, column=3)
Entry(root, textvariable=payment_mode).grid(row=5, column=3)
Checkbutton(root, variable=mealOnTheWay, text="Meal On The Way").grid(row=6, column=3)

Button(root, text="SUBMIT", command=submit).grid(row=7, column=3, pady=15)

confirm = Label(root, text="")
confirm.grid(row=8, column=3)
root.mainloop()
