def read_input():
    with open("input/day1-ex1.txt", "r") as file:
        data = file.read().split()
        return [int(digit) for digit in data]


def exercise_one():
    entries = read_input()
    for first_index, first_element in enumerate(entries):
        for second_index, second_element in enumerate(entries):
            if first_index != second_index and first_element + second_element == 2020:
                return first_element * second_element


def exercise_two():
    entries = read_input()
    for first_index, first_element in enumerate(entries):
        for second_index, second_element in enumerate(entries):
            for third_index, third_element in enumerate(entries):
                if first_index != second_index \
                        and first_index != third_index \
                        and second_element != third_index \
                        and first_element + second_element + third_element == 2020:
                    return first_element * second_element * third_element


print(exercise_two())