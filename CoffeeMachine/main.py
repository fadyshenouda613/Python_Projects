from data import MENU, resources


def report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def coin_process():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def check_sufficiency(num):
    if num == 1:
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            return f"Sorry there is not enough water."
        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            return f"Sorry there is not enough Coffee."
        else:
            return '0'
    elif num == 2:
        if resources['water'] < MENU['latte']['ingredients']['water']:
            return f"Sorry there is not enough water."
        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            return f"Sorry there is not enough Coffee."
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            return f"Sorry there is not enough milk."
        else:
            return '0'
    elif num == 3:
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            return f"Sorry there is not enough water."
        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            return f"Sorry there is not enough Coffee."
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            return f"Sorry there is not enough milk."
        else:
            return '0'


def check_transaction(amount, drink_price):
    if amount < drink_price:
        print("Sorry that is not enough money. Money Refunded.")
        return 0
    elif amount > drink_price:
        print(f"Your change is ${str(round(amount - drink_price, 2))}.")
        return drink_price
    else:
        return drink_price


def make_coffee(drink_name, order_ingridients):
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {drink_name} ☕.")


def main():
    money = 0.0
    end = False
    while not end:
        coffee = input("What would you like? (espresso/latte/cappuccino)").lower()
        if coffee == "off":
            end = True
            continue
        elif coffee == "report":
            report(money)
            continue
        elif coffee == "espresso":
            sufficiency = check_sufficiency(1)
        elif coffee == "latte":
            sufficiency = check_sufficiency(2)
        elif coffee == "cappuccino":
            sufficiency = check_sufficiency(3)
        if sufficiency != '0':
            print(sufficiency)
            continue
        money += check_transaction(coin_process(), MENU[coffee]["cost"])
        make_coffee(coffee, MENU[coffee]["ingredients"])


main()
