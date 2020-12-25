def read_groups():
    with open("input/day6-ex1.txt", "r") as file:
        data = file.read().rstrip().split("\n\n")
        return [group.split("\n") for group in data]


def count_group_anyone(group):
    yes_answers = set()
    for person in group:
        for answer in person:
            yes_answers.add(answer)
    return len(yes_answers)


def count_group_everyone(group):
    sets = [set(person) for person in group]
    result = sets[0]
    for s in sets:
        result = result & s
    return len(result)


def exercise_one():
    groups = read_groups()
    return sum(map(lambda group: count_group_anyone(group), groups))


def exercise_two():
    groups = read_groups()
    return sum(map(lambda group: count_group_everyone(group), groups))


print(exercise_two())
