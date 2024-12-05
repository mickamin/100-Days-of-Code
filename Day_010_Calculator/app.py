# Creating the Calculator 

import os
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print(logo)
    end = False
    first = float(input("What is the first number?: "))
    
    for operator in operations:
        print(operator)
    
    while not end:
        operation_symbol = input("Pick an operation: ")
        second = float(input("What is the next number?: "))
        
        operation_function = operations.get(operation_symbol)
        
        if operation_function:
            result = operation_function(first, second)
            if result is None:
                continue
            print(f"{first} {operation_symbol} {second} = {result}")
            
            choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()
            
            if choice == "y":
                first = result
            elif choice == "n":
                clear_screen()
                calculator()
                end = True
            else:
                print("Invalid input. Exiting program.")
                end = True
        else:
            print("Invalid operation. Please try again.")
            continue

calculator()