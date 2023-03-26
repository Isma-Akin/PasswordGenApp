import string
import secrets
from tkinter import *

main_win = Tk()
main_win.title("Password Generator")
main_win.geometry("800x600")

frame = Frame(main_win)
frame.pack()

alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    # print(password)
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break


def gen_pass():
    password_length = password_length_scale.get()
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(int(password_length)))

        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    # print(password)
    new_pass.delete(0, END)
    new_pass.insert(0, password)


def copy_to_clipboard():
    main_win.clipboard_clear()
    pswd = new_pass.get()
    main_win.clipboard_append(pswd)


title_label = Label(frame, text="Password Generator", font=("Arial", 30))
title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

choose_length = Label(frame, text="Choose the length of your password: ", font=("Arial", 20))
choose_length.grid(row=1, column=0, sticky="news", pady=20)

password_length_scale = Scale(frame, from_=8, to=32, orient=HORIZONTAL, length=300, font=("Arial", 20))
password_length_scale.grid(row=1, column=1, sticky="news", pady=20)

generate_pass_button = Button(frame, text="Generate Password", font=("Arial", 20), command=gen_pass)
generate_pass_button.grid(row=2, column=0, columnspan=2, pady=20)

new_pass = Entry(frame, show="*", font=("Arial", 20), width=35)
new_pass.grid(row=3, column=0, columnspan=2, sticky="news", pady=20)

copy_pass_button = Button(frame, text="Copy Password", font=("Arial", 20), command=copy_to_clipboard)
copy_pass_button.grid(row=4, column=0, columnspan=2, pady=20)

main_win.mainloop()
