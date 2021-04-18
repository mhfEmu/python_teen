# This is Coffee Maker Version 2

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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are not sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coin_processor():
    """Returns the total calculation from coin inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if transaction successful, False if not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice}. Enjoy!")


# TODO: 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # TODO: 2: Turn off the Coffee Machine by entering “Off” to the prompt.
    if choice == "off":
        is_on = False

    # TODO: 3: Print Report
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

        # TODO: 4: Check resources sufficient?
        print("Sorry there is not enough water.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # TODO: 5: Process coins
            # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

            payment = coin_processor()

            # TODO: 6: Check transaction successful?
            # Sorry that's not enough money. Money refunded.
            # Here is $2.45 dollars in change.
            if is_transaction_successful(payment, drink["cost"]):
                # TODO: 7: Make Coffee
                make_coffee(choice, drink["ingredients"])
# Program Ended
