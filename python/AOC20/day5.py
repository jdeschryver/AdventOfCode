import math


def find_seat(seat_partitioning, row, column):
    if len(seat_partitioning) == 0:
        return {
            "row": row[0],
            "column": column[0]
        }

    next_char = seat_partitioning[0]
    if next_char == "F":
        new_row = [row[0], find_center_floor(row[0], row[1])]
        return find_seat(seat_partitioning[1:], new_row, column)
    elif next_char == "B":
        new_row = [find_center_round(row[0], row[1]), row[1]]
        return find_seat(seat_partitioning[1:], new_row, column)
    elif next_char == "L":
        new_column = [column[0], find_center_floor(column[0], column[1])]
        return find_seat(seat_partitioning[1:], row, new_column)
    elif next_char == "R":
        new_column = [find_center_round(column[0], column[1]), column[1]]
        return find_seat(seat_partitioning[1:], row, new_column)


def find_center_floor(lower_bound, upper_bound):
    if lower_bound + 1 == upper_bound:
        return lower_bound
    return math.floor(find_center(lower_bound, upper_bound))


def find_center_round(lower_bound, upper_bound):
    if lower_bound + 1 == upper_bound:
        return upper_bound
    return round(find_center(lower_bound, upper_bound))


def find_center(lower_bound, upper_bound):
    return lower_bound + (upper_bound - lower_bound) / 2


def find_seat_id(partitioning):
    seat = find_seat(partitioning, [0, 127], [0, 7])
    return seat["row"] * 8 + seat["column"]


def read_input():
    with open("input/day5-ex1.txt", "r") as file:
        return [partitioning for partitioning in file.read().split()]


def exercise_one():
    partitioning_list = read_input()
    highest_id = max(map(lambda partitioning: find_seat_id(partitioning), partitioning_list))
    return highest_id


def exercise_two():
    partitioning_list = read_input()
    seat_ids = sorted(map(lambda partitioning: find_seat_id(partitioning), partitioning_list))
    filtered = list(filter(lambda seat_id:
                      ((seat_id + 1) not in seat_ids and (seat_id - 1) in seat_ids) or
                      ((seat_id + 1) in seat_ids and (seat_id - 1) not in seat_ids), seat_ids))
    return filtered[1] + 1


print(exercise_two())
