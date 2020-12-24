from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry3.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # messagebox.showinfo(title="Title", message="message")
    if len(entry1.get()) == 0 or len(entry2.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields!")
    else:
        ok = messagebox.askokcancel(title=entry1.get(), message=f"These are your info: \nEmail: {entry2.get()} \nPassword: "
                                                           f"{entry3.get()} \nDo you want to save?")
        if ok:
            file = open("data.txt", "a")
            file.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()}\n")
            entry1.delete(0, END)
            entry3.delete(0, END)
            file.close()

# ---------------------------- UI SETUP ------------------------------- #


FONT = ("Arial", 20, "normal")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

lable1 = Label(text="Website:", anchor="center", font=FONT)
lable1.grid(column=0, row=1)

lable2 = Label(text="Email/Username:", anchor="center", font=FONT)
lable2.grid(column=0, row=2)

lable3 = Label(text="Password:", anchor="center", font=FONT)
lable3.grid(column=0, row=3)

entry1 = Entry(width=43)
entry1.grid(column=1, row=1, columnspan=2, sticky=W)
entry1.focus()

entry2 = Entry(width=43)
entry2.grid(column=1, row=2, columnspan=2, sticky=W)
entry2.insert(END, "olia@gmail.com")

entry3 = Entry(width=21, justify="left")
entry3.grid(column=1, row=3, sticky=W)


button1 = Button(text="Generate Password", width=16, font=FONT, command=generate_password)
button1.grid(column=2, row=3, sticky=W)

button2 = Button(text="Add", width=33, font=FONT, command=save)
button2.grid(column=1, row=4, columnspan=2, sticky=W)


window.mainloop()