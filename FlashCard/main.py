from tkinter import *
from PIL import ImageTk, Image
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# +-------------- Read CSV & Create DICT --------------+
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# +-------------- Generates a new card--------------+
def learned():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    generate_word()


# +-------------- Generates a new card--------------+
def generate_word():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = screen.after(3000, func=flip_card)


# +-------------- Flips the card (Shows translation) --------------+
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# +-------------- UI --------------+
screen = Tk(screenName="Flash Card")
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, command=generate_word)
unknown_button.grid(row=1, column=0)
unknown_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=learned)
known_button.grid(row=1, column=1)
known_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
generate_word()
screen.mainloop()
