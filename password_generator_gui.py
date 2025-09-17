import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string
import os

# Function to select file or app
def select_file():
    filepath = filedialog.askopenfilename(
        title="Select File or Application",
        filetypes=[("All Files", "*.*")]
    )
    if filepath:
        file_var.set(filepath)

# Function to generate password
def generate_password():
    filepath = file_var.get().strip()
    username = username_entry.get().strip()

    if not filepath:
        messagebox.showerror("Missing Info", "Please select a file/app first.")
        return

    if not username:
        messagebox.showerror("Missing Info", "Please enter Username/Email first.")
        return

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Function to save password
def save_password():
    filepath = file_var.get().strip()
    username = username_entry.get().strip()
    password = result_var.get()

    if not filepath or not username or not password:
        messagebox.showerror("Missing Info", "Please select file/app, enter username, and generate password first.")
        return

    # Save to local vault file
    vault_file = "password_vault.txt"
    with open(vault_file, "a") as file:
        file.write(f"File/App: {filepath}, Username: {username}, Password: {password}\n")

    messagebox.showinfo("Saved", f"Password linked to {os.path.basename(filepath)} saved in {vault_file} ✅")
    username_entry.delete(0, tk.END)
    result_var.set("")
    file_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("450x450")
root.resizable(False, False)

# File/App Selection
tk.Label(root, text="Select File/App:").pack(pady=2)
file_var = tk.StringVar()
tk.Entry(root, textvariable=file_var, width=40, state="readonly").pack()
tk.Button(root, text="Browse", command=select_file).pack(pady=5)

# Username
tk.Label(root, text="Username/Email:").pack(pady=2)
username_entry = tk.Entry(root, width=30)
username_entry.pack()

# Length
tk.Label(root, text="Password Length:").pack(pady=2)
length_entry = tk.Entry(root, width=10)
length_entry.pack()

# Options
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output field
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack(pady=5)

# Save Button
tk.Button(root, text="Save Password", command=save_password).pack(pady=10)

root.mainloop()

