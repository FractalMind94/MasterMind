# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:51:48 2024

@author: KOM
"""

import random
import tkinter as tk
from tkinter import messagebox

colours = ["red", "blue", "green", "yellow", "white", "black"]
rand_colours = [random.choice(colours) for _ in range(4)]


def check_guess():
    global attempts
    guess = entry.get().split()
    if len(guess) != 4 or any(c not in colours for c in guess):
        messagebox.showerror("Error", "Invalid input! Please enter 4 valid colors.")
        return

    compare = []
    for i in range(len(guess)):
        if guess[i] == rand_colours[i]:
            compare.append("black")
            if compare == ['black', 'black', 'black', 'black']:
                messagebox.showinfo("Congratulations", "Good Job, You Won!")
                # root.destroy()
                rematch_prompt()
                return
        elif guess[i] in rand_colours:
            compare.append("white")

    compare.sort()
    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    guess_history_text.config(state=tk.NORMAL)
    guess_history_text.insert(tk.END, f"{', '.join(guess)} - {', '.join(compare)}\n")
    guess_history_text.config(state=tk.DISABLED)

    if attempts >= 12:
        messagebox.showinfo("Game Over", "Too Bad, You Lost!")
        # root.destroy()
        rematch_prompt()
        
def rematch_prompt():
    if messagebox.askyesno("Rematch", "Do you want to play again?"):
        reset_game()
    else:
        root.destroy()


def reset_game():
    global attempts, rand_colours
    attempts = 0
    rand_colours = [random.choice(colours) for _ in range(4)]
    attempts_label.config(text="Attempts: 0")
    guess_history_text.config(state=tk.NORMAL)
    guess_history_text.delete("1.0", tk.END)
    guess_history_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("MasterMind")

attempts = 0

attempts_label = tk.Label(root, text="Attempts: 0")
attempts_label.pack()

entry_frame = tk.Frame(root)
entry_frame.pack()

entry_label = tk.Label(entry_frame, text="Enter your guess:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(entry_frame, width=50)
entry.grid(row=0, column=1)

submit_button = tk.Button(entry_frame, text="Submit", command=check_guess)
submit_button.grid(row=0, column=2)

guess_history_frame = tk.Frame(root)
guess_history_frame.pack()

guess_history_label = tk.Label(guess_history_frame, text="Guess History:")
guess_history_label.grid(row=0, column=0)

guess_history_text = tk.Text(guess_history_frame, width=50, height=12, state=tk.DISABLED)
guess_history_text.grid(row=1, column=0)

root.mainloop()