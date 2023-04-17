import tkinter as tk
from tkinter import ttk
import random

def generate_password():
    length = length_entry.get()
    use_special_chars = special_chars_var.get()
    use_digits = digits_var.get()
    use_letters = letters_var.get()

    password_chars = []
    if use_special_chars:
        password_chars += list("!@#$%^&*()_+")
    if use_digits:
        password_chars += list("0123456789")
    if use_letters:
        password_chars += list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    if not password_chars:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Please select at least one character type.")
        return
    
    password = "".join(random.sample(password_chars, int(length)))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Şifre Oluşturma")

# Şifre uzunluğu
length_label = ttk.Label(root, text="Şifre Uzunluğu:")
length_label.grid(column=0, row=0, padx=10, pady=10)

length_entry = ttk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(column=1, row=0, padx=10, pady=10)

# Özel Karakter
special_chars_var = tk.BooleanVar(value=True)

special_chars_check = ttk.Checkbutton(root, text="Özel Karakter", variable=special_chars_var)
special_chars_check.grid(column=0, row=1, padx=10, pady=10)

# Sayı
digits_var = tk.BooleanVar(value=True)

digits_check = ttk.Checkbutton(root, text="Sayı", variable=digits_var)
digits_check.grid(column=1, row=1, padx=10, pady=10)

# Harf
letters_var = tk.BooleanVar(value=True)

letters_check = ttk.Checkbutton(root, text="Harf", variable=letters_var)
letters_check.grid(column=2, row=1, padx=10, pady=10)

# Oluştur Butonu
generate_button = ttk.Button(root, text="Oluştur", command=generate_password)
generate_button.grid(column=1, row=2, padx=10, pady=10)

# Password display
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=3, padx=10, pady=10)

password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=3, padx=10, pady=10)

root.mainloop()
