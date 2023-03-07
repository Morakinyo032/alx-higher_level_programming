#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
    last_digit = number % 10
    number = -1 * number
else:
    last_digit = number % 10
if last_digit < 6 and last_digit != 0:
    last_word = "and is less than 6 and not 0"
elif last_digit > 5:
    last_word = "and is greater than 5"
elif last_digit == 0:
    last_word = "and is 0"
print(f"Last digit of {number:d} is {last_digit:d} {last_word}")
