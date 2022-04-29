from art import logo

operations = ['+', '-', '*', '/']


def add(num1, num2):
    """Adds two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Divides two numbers"""
    return num1 / num2


def main():
    end = False
    while not end:
        print(logo)
        num1 = float(input("What's the first number?: "))
        continue_with_number = True
        for operation in range(0, len(operations)):
            print(operations[operation])
        while continue_with_number:
            operation = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
            if operation == '+':
                output = add(num1, num2)
                print(f"{num1} + {num2} = {output}")
            elif operation == '-':
                output = subtract(num1, num2)
                print(f"{num1} - {num2} = {output}")
            elif operation == '*':
                output = multiply(num1, num2)
                print(f"{num1} * {num2} = {output}")
            elif operation == '/':
                output = divide(num1, num2)
                print(f"{num1} / {num2} = {output}")
            should_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new "
                                    "calculation: ").lower()
            if should_continue == 'y':
                continue_with_number = True
                num1 = output
            else:
                break


main()
