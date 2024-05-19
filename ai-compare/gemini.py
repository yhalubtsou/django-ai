import math

def calculate(operation, num1, num2):
  """
  Performs basic mathematical operations.

  Args:
      operation: The mathematical operation to perform (add, subtract, multiply, divide).
      num1: The first number.
      num2: The second number (not required for unary operations).

  Returns:
      The result of the operation.
  """
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operation")
    return None

def scientific_functions(function, number, base=None):  # Add optional base argument
  """
  Performs scientific mathematical functions.

  Args:
      function: The scientific function to perform (sin, cos, tan, etc.).
      number: The number to perform the function on.
      base: The base for logarithm (optional, default base 10).

  Returns:
      The result of the scientific function.
  """
  if function == "sin":
    return math.sin(number)
  elif function == "cos":
    return math.cos(number)
  elif function == "tan":
    return math.tan(number)
  elif function == "log":
    if base is None:
      return math.log10(number)  # Default base 10 logarithm
    else:
      try:
        return math.log(number, base)  # Use math.log for any base
      except ValueError:
        print("Invalid base for logarithm")
        return None
  elif function == "exp":
    return math.exp(number)
  elif function == "sqrt":
    return math.sqrt(number)
  else:
    print("Invalid scientific function")
    return None

def main():
  """
  The main function that runs the calculator loop.
  """
  while True:
    # Get user input
    expression = input("Enter expression (e.g., 2 + 3, sin(45)): ")

    # Split expression
    parts = expression.split()

    # Check for scientific functions
    if len(parts) == 2 and parts[1] in ["sin", "cos", "tan", "log", "exp", "sqrt"]:
      function = parts[1]
      number = float(parts[0])
      if function == "log":
        if len(parts) == 3:
          try:
            base = float(parts[2])
            result = scientific_functions(function, number, base)
          except ValueError:
            print("Invalid base for logarithm")
            result = None
        else:
          result = scientific_functions(function, number)
      else:
        result = scientific_functions(function, number)
    # Check for basic operations
    elif len(parts) == 3 and parts[1] in ["+", "-", "*", "/"]:
      try:
        operation = parts[1]
        num1 = float(parts[0])
        num2 = float(parts[2])
        result = calculate(operation, num1, num2)
      except ValueError:
        print("Invalid number format")
        result = None
    else:
      print("Invalid expression format")
      continue

    # Print result
    if result is not None:
      print("Result:", result)

    # Ask user to continue
    choice = input("Continue? (y/n): ")
    if choice.lower() != "y":
      break

if __name__ == "__main__":
  main()
