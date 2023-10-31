#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print(f"{number} is zero")
elif number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
