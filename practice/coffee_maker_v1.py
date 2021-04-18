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
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def coffee_cost(name):
    cost1 = MENU[name]["cost"]
    return cost1


def coffee_water(name):
    need_water = MENU[name]["ingredients"]["water"]
    return need_water


def coffee_milk(name):
    need_milk = MENU[name]["ingredients"]["milk"]
    return need_milk


def coffee_raw(name):
    need_raw = MENU[name]["ingredients"]["coffee"]
    return need_raw


# TODO: 4 Check resource sufficient?
def resource_calculator(name):
    """Calculate Current Resources"""
    if name == "espresso":
        if coffee_water(name) > water:
            return "Sorry there is not enough water."
        elif coffee_raw(name) > coffee:
            return "Sorry there is not enough coffee."

    elif name == "latte" or name == "cappuccino":
        if coffee_water(name) > water:
            return "Sorry there is not enough water."
        elif coffee_raw(name) > coffee:
            return "Sorry there is not enough coffee."
        elif coffee_milk(name) > milk:
            return "Sorry there is not enough milk."

    else:
        return False


# TODO: 5 Process coins
def coin_processor(name):
    n_quarters = int(input("how many quarters?: ")) * 0.25
    n_dimes = int(input("how many dimes?: ")) * 0.10
    n_nickles = int(input("how many nickles?: ")) * 0.05
    n_pennies = int(input("how many pennies?: ")) * 0.01

    total = n_pennies + n_quarters + n_nickles + n_dimes

    cost = coffee_cost(name)

    # TODO: 6 Check transaction successful?
    if cost > total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cost < total:
        print(f"Here is ${total - cost} in change.\nHere is your {name} ☕️. Enjoy! ☕☕☕☕☕")
    elif cost == total:
        print(f"Here is your {name} ☕️. Enjoy! ☕☕☕☕☕")


def report():
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")


# TODO: 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# TODO: 7 Make Coffee
turn_coffee_machine_on = True

while turn_coffee_machine_on:
    what_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if what_coffee == "espresso":
        e_water = coffee_water("espresso")
        e_raw = coffee_raw("espresso")
        e_cost = coffee_cost("espresso")

        if not resource_calculator("espresso"):
            coin_processor("espresso")
            water -= e_water
            coffee -= e_raw
            money += e_cost
        else:
            res_printing = resource_calculator("espresso")
            print(res_printing)

    elif what_coffee == "latte":
        l_water = coffee_water("latte")
        l_milk = coffee_milk("latte")
        l_raw = coffee_raw("latte")
        l_cost = coffee_cost("latte")

        if not resource_calculator("latte"):
            coin_processor("latte")
            water -= l_water
            milk -= l_milk
            coffee -= l_raw
            money += l_cost
        else:
            res_printing = resource_calculator("latte")
            print(res_printing)

    elif what_coffee == "cappuccino":
        c_water = coffee_water("cappuccino")
        c_milk = coffee_milk("cappuccino")
        c_raw = coffee_raw("cappuccino")
        c_cost = coffee_cost("cappuccino")

        if not resource_calculator("cappuccino"):
            coin_processor("cappuccino")
            water -= c_water
            milk -= c_milk
            coffee -= c_raw
            money += c_cost
        else:
            res_printing = resource_calculator("cappuccino")
            print(res_printing)

    # TODO: 2 Turn off the Coffee Machine by entering “off” to the prompt.
    # TODO: 3 Print Report
    elif what_coffee == "off":
        turn_coffee_machine_on = False
        exit()

    elif what_coffee == "report":
        report()