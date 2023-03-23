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


def is_resource_sufficient(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


def cost():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transcation(money, drink_cost):
    if money >= drink_cost:
        global money_earned
        change = round(money - drink_cost, 2)
        print(f"Here is your ${change} change.")
        money_earned += drink_cost
        return True
    else:
        print("Not enough money. Money refunded")
        return False

def make_coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"Here is your {drink_name}")

money_earned = 0
loop = True
while loop:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if choice == "off":
        loop = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_earned}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = cost()
            if transcation(payment, drink['cost']):
                make_coffee(choice,drink["ingredients"])
        else:
            loop=False