import re


def parse_bag(bag):
    bag_info = bag.split("contain")
    global_content = {}

    if len(bag_info) < 2:
        print()

    if bag_info[1] == " no other bags.":
        return [bag_info[0], global_content]

    bag_regex = "bag(s)?[\s.]?"
    smaller_bags = re.sub(bag_regex, "", bag_info[1][1:]).lstrip().rstrip()
    encapsulating_bag = re.sub(bag_regex, "", bag_info[0]).lstrip().rstrip()

    for smaller_bag in smaller_bags.split(","):
        color_info = smaller_bag.rstrip().lstrip().split(" ", 1)
        global_content[color_info[1]] = color_info[0]

    return [encapsulating_bag, global_content]


def read_bags():
    with open("input/day7-ex1.txt", "r") as file:
        data = file.read().rstrip().split("\n")
        bags = {}
        for bag in data:
            parsed_bag = parse_bag(bag)
            bags[parsed_bag[0]] = parsed_bag[1]

        return bags


def can_contain_color(color, bag, bags):
    if bag.get(color, False):
        return True

    for deeper_color in bag:
        next_bag = bags.get(deeper_color, False)
        if next_bag and can_contain_color(color, next_bag, bags):
            return True

    return False


def number_of_bags_fitting(color, bags):
    suited_bags = 0
    for _, bag_content in bags.items():
        contains_color = can_contain_color(color, bag_content, bags)
        if contains_color:
            suited_bags += 1
    return suited_bags


def bags_needed_for(color, bags):
    bags_needed = 0
    bag = bags.get(color, False)
    if not bag:
        return 0
    for next_bag, number_of_bags in bag.items():
        bags_needed += int(number_of_bags)
        bags_needed += int(number_of_bags) * bags_needed_for(next_bag, bags)
    return bags_needed


def exercise_one():
    bags = read_bags()
    return number_of_bags_fitting("shiny gold", bags)


def exercise_two():
    bags = read_bags()
    return bags_needed_for("shiny gold", bags)


print(exercise_two())
