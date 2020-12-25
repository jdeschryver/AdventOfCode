def read_input():
    with open("input/day3-ex1.txt", "r") as file:
        data = file.read().split()
        return [list(line) for line in data]


def count_trees(map, step_x, step_y):
    max_y = len(map)
    max_x = len(map[0])
    x = 0
    y = 0

    number_of_trees = 0
    while y < max_y:
        if map[y][x % max_x] == "#":
            number_of_trees += 1
        x += step_x
        y += step_y
    return number_of_trees


def exercise_one():
    return count_trees(read_input(), 3, 1)


def exercise_two():
    traversal_one = count_trees(read_input(), 1, 1)
    traversal_two = count_trees(read_input(), 3, 1)
    traversal_three = count_trees(read_input(), 5, 1)
    traversal_four = count_trees(read_input(), 7, 1)
    traversal_five = count_trees(read_input(), 1, 2)

    return traversal_one * traversal_two * traversal_three * traversal_four * traversal_five


print(exercise_two())
