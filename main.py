from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

drinks = menu.get_items()

while is_on:
    user_input = input(f"What would you like to drink? {drinks}: ")
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        exit()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
