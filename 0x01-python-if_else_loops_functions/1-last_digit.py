#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of {:d}".format(number), end=' ')

if number < 0:
    last = (-1 * number) % 10
else:
    last = number % 10

print("is {:d} and is".format(last), end=' ')

if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0")
