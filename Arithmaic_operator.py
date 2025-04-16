# Taking input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Arithmetic operations
print(f"\nArithmetic Operations between {a} and {b}:")

print(f"Addition (+): {a} + {b} = {a + b}")
print(f"Subtraction (-): {a} - {b} = {a - b}")
print(f"Multiplication (*): {a} * {b} = {a * b}")
print(f"Division (/): {a} / {b} = {a / b if b != 0 else 'Undefined (division by zero)'}")
print(f"Floor Division (//): {a} // {b} = {a // b if b != 0 else 'Undefined'}")
print(f"Modulus (%): {a} % {b} = {a % b if b != 0 else 'Undefined'}")
print(f"Exponentiation (**): {a} ** {b} = {a ** b}")