def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def calculator():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    ch = input("Enter Your Choice: ")
    if ch not in ('1', '2', '3', '4'):
        print("Invalid choice")
        return
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if ch == '1':
        result = add(n1, n2)
        print(f"Result={result}")
    elif ch == '2':
        result = subtract(n1, n2)
        print(f"Result= {result}")
    elif ch == '3':
        result = multiply(n1, n2)
        print(f"Result = {result}")
    elif ch == '4':
        result = divide(n1, n2)
        print(f"Result= {result}")

if __name__ == "__main__":
    calculator()
