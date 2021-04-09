import re


def read_operations():
    with open("input/day14-ex1.txt") as data:
        lines = data.read().rstrip().split("\n")
    operations = []
    mask = ""
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        elif line.startswith("mem"):
            location = int(re.match(r"^mem\[(\d+)", line).group(1))
            value = int(re.match(r"^.* (\d+)$", line).group(1))
            operations.append([location, value, mask])

    return operations


def mask_without_floating(mask, value):
    mask_one = int(mask.replace("X", "0"), 2)
    mask_zero = int(mask.replace("X", "1"), 2)
    return (value | mask_one) & mask_zero


def make_all_masks(mask, all_masks):
    if "X" not in mask:
        all_masks.append(int(mask, 2))
        return all_masks
    first_mask = mask.replace("X", "0", 1)
    make_all_masks(first_mask, all_masks)
    second_mask = mask.replace("X", "1", 1)
    make_all_masks(second_mask, all_masks)


def mask_with_floats(mask, value):
    mask_zero = int(mask.replace("X", "0"), 2)
    masked_value = list('{:036b}'.format(value | mask_zero))
    for index in range(0, len(mask)):
        if mask[index] == "X":
            masked_value[index] = "X"
    masked_value = ''.join(masked_value)

    all_addresses = []
    make_all_masks(masked_value, all_addresses)

    return all_addresses


def exercise_one():
    operations = read_operations()
    mem = {}
    for operation in operations:
        mem[operation[0]] = mask_without_floating(operation[2], operation[1])


def exercise_two():
    operations = read_operations()
    mem = {}
    for operation in operations:
        addresses = mask_with_floats(operation[2], operation[0])
        for address in addresses:
            mem[address] = operation[1]
    return sum(mem.values())


print exercise_two()
