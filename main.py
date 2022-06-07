from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power_on = True

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while power_on:
    # TODO: 1. Prompt user
    menu_items = menu.get_items()
    choice = input(f"What would you like? ({menu_items}):")

    # TODO: 2. Turn off the Coffee Machine
    if choice == "off":
        power_on = False

    # TODO: 3. Print report.
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()

    # TODO: 4. Check resources sufficient?
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            # TODO: 5. Process coins.
            # TODO: 6. Check transaction successful?
            if money_machine.make_payment(drink.cost):
                # TODO: 7. Make Coffee.
                coffee_machine.make_coffee(drink)


