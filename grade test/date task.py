import simpledate
from simpledate import currentday, currentmonth


def birthday(d, m):
    currentday()
    currentmonth()

    if d == currentday() and m == currentmonth():
        print("Today is your birthay!")
    else:
        print("today is not your birthday sorry!")



birthday(21,11)