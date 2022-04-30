import random
from game_data import data
from art import logo, vs


def random_num():
    return random.randint(0, len(data))


def higher_or_lower(num1, num2, user_decision):
    if num1 > num2 and user_decision == 'a':
        return 1
    elif num2 > num1 and user_decision == 'b':
        return 2
    else:
        return 0


def main():
    end = False
    while not end:
        print(logo)
        num1 = random_num()
        while True:
            num2 = random_num()
            print(
                f"Compare A: {data[num1].get('name')}, {data[num1].get('description')}, from {data[num1].get('country')}.")
            print(vs)
            print(
                f"Compare B: {data[num2].get('name')}, {data[num2].get('description')}, from {data[num2].get('country')}.")
            user_decision = input("Who has more follower? Type 'A' or 'B': ").lower()
            result = higher_or_lower(data[num1].get('follower_count'), data[num2].get('follower_count'), user_decision)
            if result == 1:
                continue
            elif result == 2:
                num1 = num2
            else:
                print("You lost. ")
                if input("Would you like to play again? type 'y' to play again or 'n' to quit: ").lower() == 'n':
                    end = True
                    break
                else:
                    break


main()
