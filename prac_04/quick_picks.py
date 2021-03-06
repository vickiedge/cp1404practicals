#relied heavily on solution for this exercise. Still not printing all quick picks

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_PER_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBER_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print("".join("{:3}".format(number) for number in quick_pick))


