from tkinter import *

import pandas
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#FFF4E0"
# creating new flash card
current_card = {}
data_dict = {}
try:
    df = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    orignal_data = pandas.read_csv("data.csv")
    data_dict = orignal_data.to_dict(orient= "records")
else:
    data_dict = df.to_dict(orient= "records")


def change_text():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    japanese_word = current_card["Japanese"]
    canvas.itemconfig(title, text="Japanese", fill="black")
    canvas.itemconfig(jp_word, text= japanese_word, fill= "black")
    canvas.itemconfig(f_img, image= front_img)
    flip_timer = window.after(3000, func= change_card)

def right_but():
    data_dict.remove(current_card)
    print(len(data_dict))
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("words_to_learn.csv", index = False)
    change_text()

def change_card():
    canvas.itemconfig(f_img, image= back_image)
    canvas.itemconfig(title, text = "English", fill= "white" )
    canvas.itemconfig(jp_word, text= current_card["English"], fill= "white")

#setting up UI
window = Tk()
window.title("Flash Card")
window.config(pady= 50, padx= 50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, func= change_card)

canvas = Canvas(height=550, width=1000, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
f_img = canvas.create_image(500, 280, image=front_img, anchor='center')
title = canvas.create_text(500, 150, text="Japanese", font=("Ariel", "40", "italic"))
jp_word = canvas.create_text(500, 280, text="", font=("Ariel", "40", "italic"))
canvas.grid(row=0, column=0, columnspan=2)
back_image = PhotoImage(file="card_back.png")

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command= change_text)
wrong_button.grid(column=0, row= 1)


right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_but)
right_button.grid(column=1, row= 1)


change_text()


window.mainloop()