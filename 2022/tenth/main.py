import re

program = open("program.txt", "r").read()


def main():
    program_lines = program.split("\n")

    cycle = 0
    x_register = 1
    record_cycles = [20, 60, 100, 140, 180, 220]

    sum_signal_strength = 0

    for _, line in enumerate(program_lines):
        required_cycles = 0

        if line == "noop":
            required_cycles += 1  # noop takes 1 cycle

        add_instr = re.match(r"addx ([-+]?[0-9]+)", line)
        term = add_instr.group(1) if add_instr else None

        if add_instr:
            required_cycles += 2  # x register addition takes 2 cycles

        taken_cycles = 0
        while taken_cycles < required_cycles:
            taken_cycles += 1
            cycle += 1

            if cycle in record_cycles:
                signal_strength = cycle * x_register
                sum_signal_strength += signal_strength

        if add_instr:
            x_register += int(term)

    print(sum_signal_strength)


if __name__ == "__main__":
    main()
