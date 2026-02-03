import math
import datetime


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def circle_area(radius):
    return math.pi * radius ** 2


def current_time():
    return datetime.datetime.now()


if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Circle area:", circle_area(7))
    print("Current time:", current_time())
