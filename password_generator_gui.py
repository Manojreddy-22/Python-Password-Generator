import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate password
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number")
        return

    if length < 4:
        messagebox.showwarning("Too Short", "Password should be at least 4 characters")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Selection Error", "Please select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.StringVar()
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

# UI layout
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password Length:").pack()
tk.Entry(root, textvariable=length_var, width=5).pack(pady=5)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor="w", padx=50)

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 14))
result_label.pack(pady=10)

root.mainloop()
