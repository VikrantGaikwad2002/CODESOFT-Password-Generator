from tkinter import *
import tkinter as tk
from tkinter import ttk
import string
import random

def generate_password():
    complexity = complexity_var.get()

    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s = []

    if complexity == "Low":
        s.extend(s1)
        s.extend(s3)
    elif complexity == "Medium":
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
    elif complexity == "High":
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
    
    random.shuffle(s)

    plen = int(length_entry.get())
    generated_password.set("".join(s[:plen]))

    result_text.config(width=len(generated_password.get()) + 2)

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, generated_password.get())
    result_text.config(state=tk.DISABLED)

# GUI 
p_gen = tk.Tk()
p_gen.title("Password Generator")
p_gen.iconbitmap('icon.ico')
p_gen.minsize(width=500, height=350)
p_gen.configure(background='cadetblue1')

# Set the font size using ttk.Style
font_size = 20
style = ttk.Style()
style.configure('TLabel', font=('Verdana', font_size))
style.configure('TButton', font=('Verdana', font_size))
style.configure('TEntry', font=('Verdana', font_size))
style.configure('TCombobox', font=('Verdana', font_size))

# Password Length Label and Entry Box
font_size = 12
label_font = ('Verdana', font_size)
length_label = tk.Label(p_gen, text="Password Length :-", width=25, height=5, font=label_font, anchor="e",bg='cadetblue1')
length_label.grid(row=0, column=0, pady=10)

length_entry = tk.Entry(p_gen, width=30)
length_entry.grid(row=0, column=1, pady=5, columnspan=2)

# Password Complexity Dropdown
complexity_label = tk.Label(p_gen, text="Password Complexity :-", width=25, height=3, font=label_font, anchor="e",bg='cadetblue1')
complexity_label.grid(row=1, column=0, pady=5)

complexity_options = ["Low", "Medium", "High"]
complexity_var = tk.StringVar(p_gen)
complexity_var.set(complexity_options[0]) 
complexity_dropdown = ttk.Combobox(p_gen, textvariable=complexity_var, height=1, width=20, values=complexity_options)
complexity_dropdown.grid(row=1, column=1, pady=5, columnspan=2)

# Generate Password Button and Result Label
generate_button = tk.Button(p_gen, text=" Generate Password ",bg='white', font=label_font, command=generate_password,background='orange')
generate_button.grid(row=2, column=0, pady=10)

# Result box
generated_password = tk.StringVar()
result_text = tk.Text(p_gen, height=1, width=20, state=tk.DISABLED, font=('Verdana', font_size))
result_text.grid(row=2, column=1, pady=10)

p_gen.mainloop()
