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

def insert_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    inserted_coins = int(input("how many quarters?:")) * 0.25
    inserted_coins += int(input("how many dimes?: ")) * 0.1
    inserted_coins += int(input("how many nickles?: ")) * 0.05
    inserted_coins += int(input("how many pennies?: ")) * 0.01
    return inserted_coins

def coin_operation(inserted_coin, drink_cost):
    if inserted_coin >= drink_cost:
        change = round(inserted_coin - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources_if_sufficient(available_res, needed_res):
    for item in needed_res:
        if needed_res[item] > available_res[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        break
    elif user_choice == 'report':
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        payment = insert_coins()
        if check_resources_if_sufficient(resources, drink["ingredients"]):
            if coin_operation(payment, drink["cost"]):
                print(f"Here is your {user_choice} ☕️. Enjoy!")
                order_ingredients = drink["ingredients"]
                for item in order_ingredients:
                    resources[item] -= order_ingredients[item]
