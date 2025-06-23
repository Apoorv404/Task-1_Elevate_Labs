from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("Type the first number: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operator = input("Type the operator: ")
        num2 = float(input("Type the second number: "))
        result = operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {result}")
        choice = input(f"Do you want to proceed with {result}? Type 'y' if yes, type 'n' to start over.")
        if choice == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
