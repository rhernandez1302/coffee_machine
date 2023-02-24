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
"""Functions subtracts water from resources"""
def water(choice):
    if choice == 'espresso':
        return total_water - 50
    elif choice == 'latte':
        return total_water - 200
    elif choice == 'cappuccino':
        return total_water - 250
"""Functions subtracts milk from resources"""
def milk(choice):
    if choice == 'espresso':
        return total_milk
    elif choice == 'latte':
        return total_milk - 150
    elif choice == 'cappuccino':
        return total_milk - 100
"""Functions subtracts coffee from resources"""
def coffee(choice):
    if choice == 'espresso':
        return total_coffee - 18
    elif choice == 'latte':
        return total_coffee - 24
    elif choice == 'cappuccino':
        return total_coffee - 24
"""Functions calculates total amount payed """
def payment(quarters, dimes, nickels, pennies):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickels = nickels * 0.05
    total_pennies = pennies * 0.01
    return total_quarters + total_pennies + total_nickels + total_dimes
"""Functions returns the total cost of choice"""
def cost(choice):
    return MENU[choice]['cost']
"""Functions returns the current report on resources"""
def report(total_water,total_milk,total_coffee):
    print(f"Water: {total_water}\nMilk: {total_milk}\nCoffee: {total_coffee}")
"""Functions returns user what resources is not enough to make selected choice"""
def enough_resources(total_water, total_milk, total_coffee):
    if total_water <= 0:
        print("Sorry not enough water")
    elif total_coffee <= 0:
        print("NSorry not coffee")
    elif total_milk <= 0:
        print("Sorry not milk")

total_water = resources['water']
total_milk = resources['milk']
total_coffee = resources['coffee']
"""Added this while loop to keep running program"""
machine_works = True
while machine_works:
    choice = input("What would you like to order(espresso/latte/cappuccino) ")
    if choice == 'report':
        report(total_water, total_milk, total_coffee)
    else:
        total_water = water(choice)
        total_milk = milk(choice)
        total_coffee = coffee(choice)
        """I did < 0 because if it equaled to 0, it means there was just enough resources to make the selected choice"""
        if total_water < 0 or total_milk < 0 or total_coffee < 0:
            enough_resources(total_water, total_milk, total_coffee)
        else:
            owe = cost(choice)
            print(f"Your {choice} will be ${owe}")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            payed = payment(quarters, dimes, nickels, pennies)
            if payed < owe:
                print(f"Sorry that is not enough to pay for your {choice}")
            else:
                change = round(payed - owe, 2)
                print(f"You payed ${payed}, your change is ${change}. Enjoy!")
