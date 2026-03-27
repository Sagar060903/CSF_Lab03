def add(a, b):
    print("Sum =", a + b)

def subtract(a, b):
    print("Difference =", a - b)

def multiply(a, b):
    print("Product =", a * b)

def divide(a, b):
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Division by zero not allowed")

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        add(a, b)
    elif choice == 2:
        subtract(a, b)
    elif choice == 3:
        multiply(a, b)
    elif choice == 4:
        divide(a, b)
    else:
        print("Invalid choice")