import re

decisions = open("decisions.txt", "r").read()


def main():
    monkey_items = []
    monkeys_touch = []

    monkeys = decisions.split("\n\n")

    for m, monkey in enumerate(monkeys):
        lines = monkey.split("\n")

        monkey_items.append([])
        monkeys_touch.append(0)

        monkey_index: int = None
        match = re.match(r"Monkey (\d):", lines[0])
        if match:
            monkey_index = int(match.group(1))

        match = re.search(r"Starting items: ((\d+)(,\s*\d+)*)*", lines[1])
        if match:
            items = [int(item) for item in match.group(1).split(", ")]
            monkey_items[monkey_index] = items

    for i in range(0, 20):
        for m, monkey in enumerate(monkeys):
            lines = monkey.split("\n")

            monkey_index: int = None
            match = re.match(r"Monkey (\d):", lines[0])
            if match:
                monkey_index = int(match.group(1))

            operation: str = None
            worry_factor = None

            match = re.search(
                r"Operation: new = old (\+|\*) (\d+|old)", lines[2])
            if match:
                operation = match.group(1)
                worry_factor = match.group(2)

            denominator: int = None
            match = re.search(r"Test: divisible by (\d+)", lines[3])
            if match:
                denominator = int(match.group(1))

            true_monkey_index: int = None
            match = re.search(r"If true: throw to monkey (\d)", lines[4])
            if match:
                true_monkey_index = int(match.group(1))

            false_monkey_index: int = None
            match = re.search(r"If false: throw to monkey (\d)", lines[5])
            if match:
                false_monkey_index = int(match.group(1))

            thrown_items = []

            for item_index, item in enumerate(monkey_items[monkey_index]):
                monkeys_touch[monkey_index] += 1
                worry_level = item

                if operation == "+":
                    if worry_factor == "old":
                        worry_level += worry_level
                    else:
                        worry_level += int(worry_factor)
                elif operation == "*":
                    if worry_factor == "old":
                        worry_level *= worry_level
                    else:
                        worry_level *= int(worry_factor)

                # worry_level //= 3  # relief

                if worry_level % denominator == 0:  # is divisible by denominator
                    monkey_items[true_monkey_index].append(worry_level)
                else:
                    monkey_items[false_monkey_index].append(worry_level)

                thrown_items.append(item_index)

            thrown_items.reverse()
            for i in thrown_items:
                monkey_items[monkey_index].pop(i)

    monkeys_touch.sort(reverse=True)

    monkey_business = monkeys_touch[0] * monkeys_touch[1]
    print(f"Monkey business: {monkey_business}")


if __name__ == "__main__":
    main()
