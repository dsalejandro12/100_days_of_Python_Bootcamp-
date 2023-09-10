from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


in_game = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while in_game:
    options = menu.get_items()
    response = input(f"What would you like? ({options}): ").lower()

    if response == "off":
        print("Thank you for availing our services! ")
        in_game = False
    elif response== "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(response)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
