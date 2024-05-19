import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero!"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot find square root of a negative number!"
    else:
        return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def natural_log(x):
    if x <= 0:
        return "Error! Cannot find natural logarithm of a non-positive number!"
    else:
        return math.log(x)

def log_base_10(x):
    if x <= 0:
        return "Error! Cannot find logarithm base 10 of a non-positive number!"
    else:
        return math.log10(x)

print("Welcome to Scientific Calculator")

while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Natural Logarithm")
    print("12. Logarithm Base 10")
    print("13. Quit")

    choice = input("\nEnter choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    if choice == '13':
        print("Thank you for using Scientific Calculator")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    elif choice in ('6', '7', '8', '9', '10'):
        num = float(input("Enter a number: "))
        if choice == '6':
            print("Result:", square_root(num))
        elif choice == '7':
            print("Result:", factorial(int(num)))
        elif choice == '8':
            print("Result:", sin(num))
        elif choice == '9':
            print("Result:", cos(num))
        elif choice == '10':
            print("Result:", tan(num))
    elif choice == '11':
        num = float(input("Enter a number: "))
        print("Result:", natural_log(num))
    elif choice == '12':
        num = float(input("Enter a number: "))
        print("Result:", log_base_10(num))
    else:
        print("Invalid input")
