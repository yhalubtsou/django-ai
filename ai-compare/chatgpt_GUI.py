import math
import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def divide():
    try:
        if float(num2.get()) == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def power():
    try:
        result.set(float(num1.get()) ** float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def square_root():
    try:
        if float(num1.get()) < 0:
            messagebox.showerror("Error", "Cannot find square root of a negative number")
        else:
            result.set(math.sqrt(float(num1.get())))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def factorial():
    try:
        result.set(math.factorial(int(num1.get())))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def natural_log():
    try:
        if float(num1.get()) <= 0:
            messagebox.showerror("Error", "Cannot find natural logarithm of a non-positive number")
        else:
            result.set(math.log(float(num1.get())))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def log_base_10():
    try:
        if float(num1.get()) <= 0:
            messagebox.showerror("Error", "Cannot find logarithm base 10 of a non-positive number")
        else:
            result.set(math.log10(float(num1.get())))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Scientific Calculator")

num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0)

num1 = tk.Entry(root)
num1.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0)

num2 = tk.Entry(root)
num2.grid(row=1, column=1)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0)

result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, state='readonly')
result_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=3, column=0)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=3, column=1)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=4, column=0)

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=4, column=1)

power_button = tk.Button(root, text="Power", command=power)
power_button.grid(row=5, column=0)

square_root_button = tk.Button(root, text="Square Root", command=square_root)
square_root_button.grid(row=5, column=1)

factorial_button = tk.Button(root, text="Factorial", command=factorial)
factorial_button.grid(row=6, column=0)

natural_log_button = tk.Button(root, text="Natural Log", command=natural_log)
natural_log_button.grid(row=6, column=1)

log_base_10_button = tk.Button(root, text="Log Base 10", command=log_base_10)
log_base_10_button.grid(row=7, column=0)

root.mainloop()
