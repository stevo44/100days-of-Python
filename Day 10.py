# Functions with outputs

# def format_name(f_name, l_name):
#     if f_name == "" and l_name == "":
#         return "No Input Given"
#     return f_name.title() + " " + l_name.title()

# first_name = input("Enter your first name:\n")
# last_name = input("Enter your last name:\n")
# # name_capital = format_name(name, "koodeVEb")
# # print(name_capital)
# name = format_name(first_name, last_name)
# print(name)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[month - 1] = 29
        return month_days[month - 1]
    return month_days[month - 1]

# year = int(input("Type the year:\n"))
# month = int(input("Type the month:\n"))
# days = day_in_month(year, month)
# print(days)

#Doc Strings: writing the meaning or core functionality of a function and displaying on hover
def format_name(f_name, l_name):
    """ Takes the first and last name and formats
    it for you in Tittle case format"""
    if f_name == "" and l_name == "":
        return "No Input Given"
    return f_name.title() + " " + l_name.title()

# name = format_name("yoo", "BANANA")
# print(name)

#Calculator
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "+": add,
    "*": multiply,
    "/": divide,
    "-": subtract,
}
def calculator():

    num1 = float(input("Type the first number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        symbol = input("Enter the Operator you want to use from above:\n")
        next_num = float(input("Type the next number: "))
        answer = operations[symbol](num1, next_num)
        print(f"{num1} {symbol} {next_num} = {answer}")
        if input(f"Do you want to continue calculating with {answer} Type 'y' or 'n' to start a new calculation?\n").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()