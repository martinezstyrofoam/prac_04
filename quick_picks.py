import random

max_lotto_numbers = 6
min_number = 1
max_number = 45

number_of_picks = int(input("How many quick picks? "))


def quick_picker():
    global number_of_picks
    while number_of_picks < 0:
        print("Invalid number")
        number_of_picks = int(input("How many quick picks? "))  # error check
    for i in range(number_of_picks):
        quick_pick = []
        for j in range(max_lotto_numbers):
            number = random.randint(min_number, max_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(
            f"{number:2}" for number in quick_pick))  # .join only works with str. the f"{}" converts int to str


quick_picker()

