import os  # TRIVIAL: unused import
import math


def a(x, y):  # TRIVIAL: unclear naming
    return x + y


def multiply(first_number, second_number):
    return first_number * second_number


def circle_area(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r