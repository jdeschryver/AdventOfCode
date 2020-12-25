def tackle_sum(positions, current_position):
    term_one = positions[positions[current_position + 1]]
    term_two = positions[positions[current_position + 2]]
    positions[positions[current_position + 3]] = term_one + term_two


def tackle_multiplication(positions, current_position):
    factor_one = positions[positions[current_position + 1]]
    factor_two = positions[positions[current_position + 2]]
    positions[positions[current_position + 3]] = factor_one * factor_two


def setup_positions(pos_one, pos_two):
    with open("input/day2-ex1.txt", "r") as file:
        data = file.read().split(',')
        positions = [int(digit) for digit in data]
        positions[1] = pos_one
        positions[2] = pos_two
        return positions


def run(positions):
    current_position = 0
    while positions[current_position] != 99:
        if positions[current_position] == 1:
            tackle_sum(positions, current_position)
        elif positions[current_position] == 2:
            tackle_multiplication(positions, current_position)
        current_position += 4


def exercise_one():
    positions = setup_positions(12, 2)
    run(positions)
    print(positions[0])


def exercise_two():
    for pos_one in range(0, 50):
        for pos_two in range(0, 50):
            positions = setup_positions(pos_one, pos_two)
            run(positions)

            if positions[0] == 19_690_720:
                print(100 * pos_one + pos_two)


exercise_two()
