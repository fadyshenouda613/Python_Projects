from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip

uppercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lowercase_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                       "s", "t", "u", "v", "w", "x", "y", "z"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    t_password.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letters_choice = [choice(letters) for _ in range(randint(8, 10))]
    numbers_choice = [choice(numbers) for _ in range(randint(2,4))]
    symbols_choice = [choice(symbols) for _ in range(randint(2,4))]
    password_list = letters_choice + numbers_choice + symbols_choice
    shuffle(password_list)
    password = "".join(password_list)
    t_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = t_website.get()
    email = t_email.get()
    password = t_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                t_website.delete(0, END)
                t_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk(screenName="Password Manager")
screen.config(pady=50, padx=100, )
screen.title("Password Manager")

img = ImageTk.PhotoImage(Image.open("logo.png"))
l_image = Label(screen, image=img)
l_image.grid(column=1, row=0)

l_website = Label(screen, text="Website:", padx=10)
l_website.grid(column=0, row=3)

t_website = Entry(width=35)
t_website.grid(column=1, row=3)
t_website.focus()

l_email = Label(text="Email/Username: ")
l_email.grid(column=0, row=4)

t_email = Entry(width=35)
t_email.grid(column=1, row=4)
t_email.insert(0, "fadysheno@gmail.com")

l_password = Label(text="Password: ")
l_password.grid(row=5, column=0)

t_password = Entry(width=35)
t_password.grid(row=5, column=1)

b_generate = Button(text="Generate Password", command=generate_password)
b_generate.grid(row=5, column=2)
b_generate.config(bd=4, bg="blue", fg="white")

b_add = Button(text="Add", width=34, fg="white", bg="blue", command=save)
b_add.grid(row=6, column=1)

screen.mainloop()
