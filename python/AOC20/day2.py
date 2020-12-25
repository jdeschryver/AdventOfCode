def process_line(line):
    line[0] = [int(bound) for bound in line[0].split("-")]
    line[1] = line[1].replace(":", "")
    return line


def read_input():
    with open("input/day2-ex1.txt", "r") as file:
        lines = [line.rstrip('\n').split() for line in file]
        return [process_line(line) for line in lines]


def is_valid_exercise_one(input_line):
    occurrence = str(input_line[2]).count(input_line[1])
    return input_line[0][0] <= occurrence <= input_line[0][1]


def is_valid_exercise_two(input_line):
    pos_one = input_line[0][0]
    pos_two = input_line[0][1]

    char = input_line[1]
    string = str(input_line[2])

    char_one = len(string) > pos_one and string[pos_one - 1] == char
    char_two = len(string) > pos_two and string[pos_two - 1] == char
    return char_one or char_two


def exercise_one():
    valid_lines = 0
    for line in read_input():
        if is_valid_exercise_one(line):
            valid_lines += 1
    return valid_lines


def exercise_two():
    valid_lines = 0
    for line in read_input():
        if is_valid_exercise_two(line):
            valid_lines += 1
    return valid_lines


print(exercise_two())
