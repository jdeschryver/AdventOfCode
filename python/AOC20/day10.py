def read_joltage_ratings():
    with open("input/day10-ex1.txt", "r") as file:
        data = file.read().rstrip().split()
        return list(map(int, data))


def find_one_three_differences(ratings):
    sorted_ratings = sorted(ratings)
    diff_one = 0
    diff_three = 0

    current_index = 0
    current_output = 0

    while current_index < len(sorted_ratings):
        if sorted_ratings[current_index] == current_output + 1:
            diff_one += 1
            current_output += 1
        elif sorted_ratings[current_index] == current_output + 3:
            diff_three += 1
            current_output += 3

        current_index += 1

    return diff_one, diff_three + 1


def exercise_two():
    ratings = read_joltage_ratings()
    ratings.sort()
    ratings.append(ratings[-1] + 3)

    memo = {0: 1}
    for r in ratings:
        memo[r] = memo.get(r - 3, 0) + memo.get(r - 2, 0) + memo.get(r - 1, 0)
    print(memo[ratings[-1]])


def exercise_one():
    ratings = read_joltage_ratings()
    diff_one, diff_three = find_one_three_differences(ratings)

    return diff_one * diff_three


print(exercise_two())
