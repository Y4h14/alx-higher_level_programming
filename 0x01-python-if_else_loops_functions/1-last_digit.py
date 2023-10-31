#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x = -10
else:
    x = 10
if number % x > 5:
    print(f"Last digit of {number} is {number % x} and is greater than 5")
elif number % x < 6:
    if number % x == 0:
        print(f"Last digit of {number} is {number % x} and is 0")
    else:
        print(f"Last digit of {number} is {number % x} and is\
 less than 6 and not 0")
