from os import system, name
from time import sleep
def clear():
      _ = system('cls')
clear()
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def substract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():

    num1 = int(input("What's your first number?"))
    for key in operations:
        print(key)

    calculation_going = True
    while calculation_going == True:
        symbol = input("Pick an operation: ")
        num2 = int(input("What's your second number?"))
        calc_function = operations[symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        next = input(f"Do you want to continue ? Type 'y' if you want to continue calculating with {answer}, type 'n' to start a new calculation.")
        if next == "y":
            num1 = answer
        if next == "n":
            calculation_going = False
            clear()
            calculator()

calculator()




