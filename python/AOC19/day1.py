import math


def calculate_fuel(mass):
    fuel = mass / 3
    return math.floor(fuel) - 2


def exercise_one():
    file = open("input/day1-ex1.txt", "r")
    sum_of_fuel = 0
    for mass in file:
        sum_of_fuel += calculate_fuel(float(mass))
    file.close()
    print(sum_of_fuel)


def exercise_two():
    file = open("input/day1-ex2.txt", "r")
    sum_of_fuel = 0
    for mass in file:
        intermediate_fuel = calculate_fuel(float(mass))
        while intermediate_fuel > 0:
            sum_of_fuel += intermediate_fuel
            intermediate_fuel = calculate_fuel(intermediate_fuel)
    file.close()
    print(sum_of_fuel)
