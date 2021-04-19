from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # TODO: 1 print report
        coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # TODO: 2 Check resource sufficient?
        # TODO: 3 Process Coins
        # TODO: 4 Check transaction successful?
        if coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            # TODO: 5 Make Coffee
            coffee_maker.make_coffee(drink)