import re


def parse_passport(passport):
    pairs = passport.split()
    mapped_fields = {}
    for pair in pairs:
        key_value = pair.split(":")
        mapped_fields[key_value[0]] = key_value[1]
    return mapped_fields


def read_passports():
    with open("input/day4-ex1.txt", "r") as file:
        data = file.read().split("\n\n")
        return [parse_passport(passport) for passport in data]


def has_all_fields(mandatory_fields, passport):
    return set(mandatory_fields).issubset(passport.keys())


def matches_regex(requirements, passport):
    for requirement in requirements:
        field = str(requirement[0])
        regex = str(requirement[1])
        value = passport.get(field, False)
        if not value:
            return False
        if not bool(re.search(regex, value)):
            return False
    return True


def exercise_one():
    passports = read_passports()
    mandatory_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    print(sum(map(lambda passport: has_all_fields(mandatory_fields, passport), passports)))


def read_passports():
    with open("input/day4-ex1.txt", "r") as file:
        data = file.read().split("\n\n")
        return [parse_passport(passport) for passport in data]


def exercise_two():
    passports = read_passports()
    requirements = [
        ["byr", "^(19[2-9]\\d|200[0-2])$"],
        ["iyr", "^(201\\d|2020)$"],
        ["eyr", "^(202\\d|2030)$"],
        ["hgt", "^(1[5-8]\\d|19[0-3])cm|(59|6\\d|7[0-6])in$"],
        ["hcl", "^#[0-9a-f]{6}$"],
        ["ecl", "^amb|blu|brn|gry|grn|hzl|oth$"],
        ["pid", "^[0-9]{9}$"]
    ]
    print(sum(map(lambda passport: matches_regex(requirements, passport), passports)))


exercise_two()
