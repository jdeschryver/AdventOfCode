import copy


def read_instructions():
    with open("input/day8-ex1.txt", "r") as file:
        data = file.read().rstrip().split("\n")
        instructions = []
        for line in data:
            instruction = line.split(" ")
            instructions.append([instruction[0], int(instruction[1])])
        return instructions


def run(instructions):
    visited_instructions = set()
    accumulator = 0
    instruction_counter = 0
    while instruction_counter < len(instructions) - 1:
        if instruction_counter in visited_instructions:
            return False, accumulator
        visited_instructions.add(instruction_counter)

        instruction = instructions[instruction_counter]
        if instruction[0] == "acc":
            accumulator += instruction[1]
            instruction_counter += 1
        elif instruction[0] == "jmp":
            instruction_counter += instruction[1]
        else:
            instruction_counter += 1
    return True, accumulator


def exercise_one():
    instructions = read_instructions()
    return run(instructions)


def exercise_two():
    instructions = read_instructions()
    copy_instructions = copy.deepcopy(instructions)
    instruction_counter = 0
    while instruction_counter < len(instructions) - 1:
        if instructions[instruction_counter][0] == "jmp":
            instructions[instruction_counter][0] = "nop"
        elif instructions[instruction_counter][0] == "nop":
            instructions[instruction_counter][0] = "jmp"

        instruction_counter += 1
        success, acc = run(instructions)

        if success:
            return acc

        instructions = copy_instructions
        copy_instructions = copy.deepcopy(instructions)
    return False


print(exercise_two())
