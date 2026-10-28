MENU = {
    "espresso":{
        "ingredients": {
            "water" : 50,
            "coffee" : 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 200,
}
# TODO 1. prompt the user what they would like
# user_input = input("what would you like? (espresso/latte/cappuccino): ")



# TODO: 2. Print report from the resource dictionary if "report"
resources["money"] = 0
def print_report():
    print(f"""
    Water:  {resources["water"]}ml
    Milk:   {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money:  {resources["money"]}$
    """)
    # for key, value in resources.items():
    #     print(f"key, value")


#TODO:3 Check sufficient resources when the user orders the drink
def check_sufficient_resources(users_choice):
    for key, value in MENU[users_choice]["ingredients"].items():
        if value > resources[key]:
            return f"Not enough {key} to make {users_choice}"
    return True

#TODO: 4 Order coffee
def coins_collector():
    coins = ["quarters", "dimes", "nickels", "pennies"]
    coins_collected = []
    print("Please insert coins")
    for coin in coins:
        coins_collected.append(int(input(f"How many {coin}?: ")))
    return coins_collected

#TODO:5 Change calculator
def coins_checker(users_choice, coins_collected):
    coins_value = [0.25, 0.10, 0.05, 0.01]
    adjusted_value = []
    for coin in range(len(coins_collected) - 1):
        adjusted_value.append(coins_value[coin] * coins_collected[coin])
    sum_coins_collected = sum(adjusted_value)
    if sum_coins_collected < MENU[users_choice]["cost"]:
        return  f"Not enough money for {users_choice}"
    return sum_coins_collected
def update_resources(user_choice):
    for key, value in MENU[user_choice]["ingredients"].items():
        resources[key] -= value
    resources["money"] += MENU[user_choice]["cost"]

def processor(coins_dollar_value, users_choice):
    user_balance = coins_dollar_value - MENU[users_choice]["cost"]
    update_resources(users_choice)
    print(f"Here is ${round(user_balance, 2)} in change")
    print(f"Here is you {users_choice} ☕, Enjoy!")

on_coffee_machine = True
def make_coffee():
    global on_coffee_machine
    user_input = input("what would you like? (espresso/latte/cappuccino): ").lower().strip()
    if user_input == "report":
        print_report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        check_ingredients = check_sufficient_resources(user_input)
        if check_ingredients is True:
            collect_coins = coins_collector()
            coin_value = coins_checker(user_input, collect_coins)
            if type(coin_value) == float:
                processor(coin_value, user_input)
            else:
                print(coin_value)
        else:
            print(check_ingredients)
    elif user_input == "off":
        on_coffee_machine = False


def coffee_machine():
    while on_coffee_machine:
        make_coffee()

coffee_machine()
