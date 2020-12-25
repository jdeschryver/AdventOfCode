def read_xmas():
    with open("input/day9-ex1.txt") as file:
        return list(map(int, file.read().rstrip().split()))


def check_number(number, window):
    for outer_index in range(0, len(window)):
        for inner_index in range(outer_index + 1, len(window)):
            if window[outer_index] + window[inner_index] == number:
                return True

    return False


def check_xmas(preamble_size, xmas):
    start_index = 0
    stop_index = preamble_size - 1

    while stop_index + 1 < len(xmas) - 1:
        number = xmas[stop_index + 1]
        if not check_number(number, xmas[start_index: stop_index + 1]):
            return number
        start_index += 1
        stop_index += 1
    return True


def find_subset_summing_to(requested_sum, xmas):
    start_index = 0
    stop_index = 0
    current_sum = 0
    while stop_index < len(xmas):
        current_sum += xmas[stop_index]
        if current_sum == requested_sum:
            return xmas[start_index: stop_index + 1]
        elif current_sum < requested_sum:
            stop_index += 1
        else:
            start_index += 1
            stop_index = start_index
            current_sum = 0
    return False


def exercise_one():
    xmas = read_xmas()
    preamble = 25
    return check_xmas(preamble, xmas)


def exercise_two():
    xmas = read_xmas()
    requested_sum = 32321523
    subset = find_subset_summing_to(requested_sum, xmas)
    return min(subset) + max(subset) if isinstance(subset, list) else False


print(exercise_two())
