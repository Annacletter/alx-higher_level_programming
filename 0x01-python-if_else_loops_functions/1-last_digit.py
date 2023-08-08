#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
final = abs(number) % 10
sign = -1 if number < 10 else 1
final *= sign

diff = (
    "greater than 5" if final > 5 else
    "less than 6 and not 0" if final != 0 else
    "0"
)
print(f"Last digit of {number} is {final} and is {diff}")
