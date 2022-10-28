import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

machine_on = True


def show_report():
    """Function that will show a report of the current resources."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


def resources_sufficient(coffee):
    """Function that will check that there is sufficient resources to make the chosen coffee."""
    if coffee == 'latte' or coffee == 'cappuccino':
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Sorry, not enough water.")
            return False
        elif resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Sorry, not enough milk.")
            return False
        elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Sorry, not enough coffee.")
            return False
        else:
            return True
    elif coffee == 'espresso':
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Sorry, not enough water.")
            return False
        elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Sorry, not enough coffee.")
            return False
        else:
            return True


def process_coins(num_quarters, num_dimes, num_nickles, num_pennies):
    """Function that calculates the value of the coins the user has entered."""
    quarters_value, dimes_value, nickles_value, pennies_value = 0, 0, 0, 0
    if num_quarters>0:
        quarters_value = num_quarters * 0.25
    if num_dimes > 0:
        dimes_value = num_dimes * 0.10
    if num_nickles > 0:
        nickles_value = num_nickles * 0.05
    if num_pennies > 0:
        pennies_value = num_pennies * 0.01

    total = quarters_value + dimes_value + nickles_value + pennies_value
    return total


def transaction(price, entered_coins):
    """Function that will check if the user has entered enough money to purchase a coffee."""
    if entered_coins > price:
        change = round(entered_coins - price,2)
        print(f"Here is ${change} in change.")
        resources['money'] += price
        return True
    else:
        return False


def make_coffee(coffee):
    """Function that will only be called if the machine has sufficient resources and the user
    entered enough money. It will give the user their coffee and remove the used ingredients from
    the resources table."""
    print(f"Here is your {coffee}, enjoy!☕")
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    if coffee == 'latte' or coffee == 'cappuccino':
        resources['milk'] -= MENU[coffee]['ingredients']['milk']


while machine_on:
    user_choice = input("What coffee would you like? Espresso/Latte/Cappuccino: ").lower()

    if user_choice == 'off':
        machine_on = False
        print("Powering off.")

    if user_choice == 'report':
        show_report()

    enough_resources = resources_sufficient(user_choice)
    if enough_resources:

        print("Please insert coins.")
        quarters_entered = int(input("How many quarters?: "))
        dimes_entered = int(input("How many dimes?: "))
        nickels_entered = int(input("How many nickels?: "))
        pennies_entered = int(input("How many pennies?: "))
        coins_entered = process_coins(quarters_entered, dimes_entered, nickels_entered, pennies_entered)

        price = MENU[user_choice]['cost']
        enough_money = transaction(price, coins_entered)

        if enough_money:
            make_coffee(user_choice)
        else:
            print("Not enough money. Money Refunded.")


