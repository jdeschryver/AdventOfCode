def read_seating():
    with open("input/day11-ex1.txt") as file:
        lines = file.read().rstrip().split("\n")
        return [list(line) for line in lines]


def new_seat(seating, row, column):
    seat = seating[row][column]

    if seat == 'L':
        if occupied_seats(seating, row, column) == 0:
            return True, '#'
    elif seat == '#':
        if occupied_seats(seating, row, column) >= 5:
            return True, 'L'

    return False, seat


def occupied_seats(seating, row, column):
    tl = is_seat_occupied(seating, row, column, -1, -1)
    tc = is_seat_occupied(seating, row, column, -1, 0)
    tr = is_seat_occupied(seating, row, column, -1, 1)
    l = is_seat_occupied(seating, row, column, 0, -1)
    r = is_seat_occupied(seating, row, column, 0, 1)
    bl = is_seat_occupied(seating, row, column, 1, -1)
    bc = is_seat_occupied(seating, row, column, 1, 0)
    br = is_seat_occupied(seating, row, column, 1, 1)

    return sum(map(lambda neighbor: int(neighbor), [tl, tc, tr, l, r, bl, bc, br]))


def is_seat_occupied(seating, row, column, row_inc, column_inc):
    new_row = row
    new_col = column
    while True:
        new_row = new_row + row_inc
        new_col = new_col + column_inc

        if len(seating) <= new_row or new_row < 0:
            return False

        if len(seating[new_row]) <= new_col or new_col < 0:
            return False

        if seating[new_row][new_col] != '.':
            return seating[new_row][new_col] == '#'


def test(seating):
    isChanged = True
    new_seating = [[None for y in range(len(seating[0]))] for x in range(len(seating))]
    while isChanged:
        isChanged = False
        for row_index, row in enumerate(seating):
            for column_index, element in enumerate(row):
                changed_cheat, new_seat_a = new_seat(seating, row_index, column_index)
                if changed_cheat:
                    isChanged = True
                new_seating[row_index][column_index] = new_seat_a
        seating = new_seating
        new_seating = [[None for y in range(len(seating[0]))] for x in range(len(seating))]
    return sum(map(lambda row: sum(map(lambda element: int(element == '#'), row)), seating))


seating = read_seating()
print test(seating)
