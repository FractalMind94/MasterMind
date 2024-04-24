# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:11:44 2024

@author: KOM
"""

import random
import tkinter as tk
from tkinter import messagebox, Label

colours = {
    "red": "#FF0000",
    "blue": "#0000FF",
    "green": "#00FF00",
    "yellow": "#FFFF00",
    "white": "#FFFFFF",
    "black": "#000000"
}

rand_colours = [random.choice(list(colours.keys())) for _ in range(4)]
# rand_colours = ["black","white","red","blue" ]
# correct_answer = ', '.join(rand_colours)
# correct_answer_text.create_rectangle(170 + i * 30, attempts * 30, 180 + i * 30, 20 + attempts * 30, fill=colours[color])

def show_correct_answer():
    answer_window = tk.Toplevel(root)
    answer_window.title("Correct Answer")

    answer_label = tk.Label(answer_window, text="Correct answer:")
    answer_label.pack(side=tk.LEFT) # Puts answer to the left

    for color in rand_colours:
        color_frame = tk.Frame(answer_window, width=30, height=30, bg=colours[color])
        color_frame.pack(side=tk.LEFT)# Pack color frames horizontally

        
def check_guess():
    
    global attempts
    
    guess = entry.get().split()
    if len(guess) != 4 or any(c not in colours.keys() for c in guess):
        messagebox.showerror("Error", "Invalid input! Please enter 4 valid colors.")
        entry.delete(0, tk.END)
        return
    entry.delete(0, tk.END)
    compare = []
    for i in range(len(guess)):
        if guess[i] == rand_colours[i]:
            compare.append("black")
            if compare == ['black', 'black', 'black', 'black']:
                messagebox.showinfo("Congratulations", "Good Job, You Won!")
                rematch_prompt()
                return
        elif guess[i] in rand_colours:
            compare.append("white")

    compare.sort()
    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    # Inserting rectangles representing the guessed colors
    for i, color in enumerate(guess):
        guess_history_text.create_rectangle(10 + i * 30, attempts * 30, 30 + i * 30, 20 + attempts * 30, fill=colours[color])

    # Inserting rectangles representing the result colors
    for i, color in enumerate(compare):
        guess_history_text.create_rectangle(170 + i * 30, attempts * 30, 180 + i * 30, 20 + attempts * 30, fill=colours[color])

    # Inserting horizontal line between guess and result sections
    guess_history_text.create_line(0, attempts * 30 + 25, 400, attempts * 30 + 25)
    # Inserting vertical line between guess and result sections
    guess_history_text.create_line(160, 0, 160, (attempts + 1) * 30 + 25)
    
    if attempts == 12:
        
        messagebox.showinfo("Game Over", "Too Bad, You Lost!")
        
        show_correct_answer() # reference to show_correct_answer function

        # DISPLAYS ANSWER IN WORDS
        # correct_answer = ', '.join(rand_colours)
        # correct_answer = "\n"
        # messagebox.showinfo("Correct Answer", )
        # messagebox.showinfo("Correct Answer", f"The correct answer was: {rand_colours}")
        # messagebox.showanswer(f"Right Answer:{rand_colours}")
        
        rematch_prompt()
        

def rematch_prompt():
    if messagebox.askyesno("Rematch", "Do you want to play again?"):
        reset_game()
    else:
        root.destroy()
    

def reset_game():
    
    
    global attempts, rand_colours
    attempts = 0
    rand_colours = [random.choice(list(colours.keys())) for _ in range(4)]
    attempts_label.config(text="Attempts: 0")
    guess_history_text.delete("all")
   
       

    
    
root = tk.Tk()
root.title("MasterMind")
def color_selected(color):
    if entry.get():  # Check if entry is not empty
        entry.insert(tk.END, ' ')  # Insert space
    entry.insert(tk.END, color)

# def submit_guess():
#     guess = entry.get().split()
#     print("Submit:", guess)
#     entry.delete(0, tk.END)
    
# root = tk.Tk()
# root.title("MasterMind")

# entry_frame = tk.Frame(root)
# entry_frame.pack()
# # Create a frame for the color buttons
# button_frame = tk.Frame(entry_frame)
# button_frame.pack(side=tk.TOP, pady=5)  # Pack the button frame at the top of the game frame

# Create buttons for each color
for color, hex_code in colours.items():
    button = tk.Button(root, bg=hex_code, width=3, height=1, command=lambda c=color: color_selected(c))
    # button.pack(root, text= "TOP")
    button.pack(side=tk.LEFT, padx=1, pady=1)
    # button.place(x=200, y=200)
    # 
attempts = 0

attempts_label = tk.Label(root, text="Attempts: 0")
attempts_label.pack()

entry_frame = tk.Frame(root)
entry_frame.pack()

entry_label = tk.Label(entry_frame, text="Enter your guess:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(entry_frame, width=30)
entry.grid(row=0, column=1)


submit_button = tk.Button(entry_frame, text="Submit", command=check_guess, width=10)
submit_button.grid(row=0, column=2)


guess_history_frame = tk.Frame(root)
guess_history_frame.pack()

guess_history_label = tk.Label(guess_history_frame, text="Guess History:")
guess_history_label.grid(row=0, column=0)

# Create a Canvas widget for the guess history
guess_history_text = tk.Canvas(guess_history_frame, width=400, height=600)
guess_history_text.grid(row=1, column=0)

    
# Enter for submitting answer    
def on_enter(event):
    check_guess()

# Bind the "Return" key to the on_enter function
root.bind("<Return>", on_enter)
root.mainloop()

