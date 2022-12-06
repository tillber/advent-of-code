import re

stacks = open("stacks.txt", "r").read()


def main():
    instructions = stacks.split("\n\n")[1].split("\n")

    stacking = stacks.split("\n\n")[0].split("\n")[:-1]
    crates = parse_crates(stacking)

    parsed_instructions = parse_instructions(instructions)

    for _, instruction in enumerate(parsed_instructions):
        crates_to_move = crates[instruction[1]][0:instruction[0]]

        # in part 2; crates remain in order when multiple are moved at once
        # (i.e. skip reverse for part 2)
        crates_to_move.reverse()

        # move crates to new stack,
        # and delete them from their origin stack
        crates[instruction[2]] = crates_to_move + crates[instruction[2]]
        del crates[instruction[1]][0:instruction[0]]

    # get code with top crates
    code = ""
    for _, stack in enumerate(crates):
        code = code + stack[0]

    print(code)


def parse_instructions(instructions):
    parsed_instructions = []
    for _, instruction in enumerate(instructions):
        match = re.match('move (\d+) from (\d+) to (\d+)', instruction)
        parsed_instructions.append([int(match.group(1)), int(
            match.group(2)) - 1, int(match.group(3)) - 1])

    return parsed_instructions


def parse_crates(stacking):
    crates = []

    for i, item in enumerate(stacking):
        # delete every fourth element (space delimiters) in list (starting from third element).
        item_arr = list(item)
        del item_arr[3::4]
        item = "".join(item_arr).replace(
            "[", "").replace("]", "").replace("   ", " ")

        for k in range(0, len(item), 1):
            crate = item[k]
            if i == 0:  # append list although stack may not contain a crate
                crate = [] if crate.isspace() else [crate]
                crates.append(crate)
            elif not crate.isspace():
                crates[k].extend([crate])

    return crates


if __name__ == "__main__":
    main()
