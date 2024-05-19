import math
import tkinter as tk


def calculate(operation, num1, num2):
    """
    Performs basic mathematical operations.

    Args:
        operation: The mathematical operation to perform (add, subtract, multiply, divide).
        num1: The first number.
        num2: The second number (not required for unary operations).

    Returns:
        The result of the operation, or None on error.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return None  # Indicate division by zero
        else:
            return num1 / num2
    else:
        return None  # Indicate invalid operation


def scientific_functions(function, number, base=None):
    """
    Performs scientific mathematical functions.

    Args:
        function: The scientific function to perform (sin, cos, tan, etc.).
        number: The number to perform the function on.
        base: The base for logarithm (optional, default base 10).

    Returns:
        The result of the scientific function, or None on error.
    """
    if function == "sin":
        return math.sin(number)
    elif function == "cos":
        return math.cos(number)
    elif function == "tan":
        return math.tan(number)
    elif function == "log":
        if base is None:
            return math.log10(number)
        else:
            try:
                return math.log(number, base)
            except ValueError:
                return None  # Invalid base
    elif function == "exp":
        return math.exp(number)
    elif function == "sqrt":
        return math.sqrt(number)
    else:
        return None  # Invalid scientific function


def button_click(char):
    """
    Handles button clicks and updates the display.
    """
    global expression
    if char == "=":
        calculate_result()
    else:
        expression += str(char)
    display_var.set(expression)


def clear_all():
    """
    Clears the display and resets the expression.
    """
    global expression
    expression = ""
    display_var.set(expression)


def calculate_result():
    """
    Evaluates the expression and displays the result or error message.
    """
    try:
        result = eval(expression)
        display_var.set(result)
        expression = str(result)  # Update expression for further calculations
    except SyntaxError:
        display_var.set("Error")
    except ZeroDivisionError:
        display_var.set("Div by Zero")
    except:  # Catch other potential errors
        display_var.set("Error")


expression = ""  # Global variable to store the expression


# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Create the display
display_var = tk.StringVar()
display = tk.Entry(window, textvariable=display_var, justify="right", width=30)
display.grid(columnspan=4)

# Create buttons for numbers and basic operations
button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
button_1.grid(row=3, column=0)
button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
button_2.grid(row=3, column=1)
button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
button_3.grid(row=3, column=2)
button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
button_7.grid(row=1, column=0)
button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
button_8.grid(row=1, column=1)
button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
button_9.grid(row=1, column=2)

button_add = tk.Button(window, text="+", command=lambda: button_click("+"))
button_add.grid(row=1, column=3)
button_sub = tk.Button(window, text="-", command=lambda: button_click("-"))
button_sub.grid(row=2, column=3)
button_mul = tk.Button(window, text="*", command=lambda: button_click("*"))
button_mul.grid(row=3, column=3)
button_div = tk.Button(window, text="/", command=lambda: button_click("/"))
button_div.grid(row=4, column=3)

# Create buttons for scientific functions
button_sin = tk.Button(window, text="sin", command=lambda: button_click("sin("))
button_sin.grid(row=5, column=0)
button_cos = tk.Button(window, text="cos", command=lambda: button_click("cos("))
button_cos.grid(row=5, column=1)
button_tan = tk.Button(window, text="tan", command=lambda: button_click("tan("))
button_tan.grid(row=5, column=2)
button_log = tk.Button(window, text="log", command=lambda: button_click("log("))
button_log.grid(row=6, column=0)
button_ln = tk.Button(window, text="ln", command=lambda: button_click("log(,"))  # ln(x) as log(x, e)
button_ln.grid(row=6, column=1)
button_exp = tk.Button(window, text="exp", command=lambda: button_click("exp("))
button_exp.grid(row=6, column=2)
button_sqrt = tk.Button(window, text="sqrt", command=lambda: button_click("sqrt("))
button_sqrt.grid(row=6, column=3)

# Clear, Equal, and other buttons (optional)
button_clear = tk.Button(window, text="C", command=clear_all)
button_clear.grid(row=1, column=4)
button_equal = tk.Button(window, text="=", command=calculate_result)
button_equal.grid(row=5, column=3)
# ... (add buttons for parentheses, memory functions, etc.)

# Main loop to keep the window running
window.mainloop()
