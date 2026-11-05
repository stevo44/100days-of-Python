from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine = True
while coffee_machine:
    menu_item = Menu.get_items(Menu())
    user_input = input(f"what would you like? ({menu_item}): ").lower()
    if user_input == "report":
        report = coffe_maker.report()
        profit = money_machine.report()
    elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        drink = menu.find_drink(user_input)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
    elif user_input == "off":
        coffee_machine = False
    else:
        drink = menu.find_drink(user_input)

