import re

decisions = open("decisions.txt", "r").read()


# class Monkey:
#     def __init__(text):
#         self.__size = size
#         self.__name = name

#     def size(self):
#         return self.__size

#     def name(self):
#         return self.__name


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

            print(monkey_items[m])

            monkey_index: int = None
            match = re.match(r"Monkey (\d):", lines[0])
            if match:
                monkey_index = int(match.group(1))

            print(f"Monkey {monkey_index}:")

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

                print(
                    f"Monkey inspects an item with a worry level of {worry_level}")

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

                worry_level //= 3  # relief
                print(
                    f"Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

                if worry_level % denominator == 0:  # is divisible by denominator
                    print(
                        f"Current worry level is divisible by {denominator}.")
                    monkey_items[true_monkey_index].append(worry_level)
                    print(
                        f"Item with worry level {worry_level} is thrown to monkey {true_monkey_index}.")
                else:
                    print(
                        f"Current worry level is not divisible by {denominator}.")
                    monkey_items[false_monkey_index].append(worry_level)
                    print(
                        f"Item with worry level {worry_level} is thrown to monkey {false_monkey_index}.")

                thrown_items.append(item_index)

            thrown_items.reverse()
            for i in thrown_items:
                monkey_items[monkey_index].pop(i)

    print(monkey_items)
    monkeys_touch.sort(reverse=True)

    monkey_business = monkeys_touch[0] * monkeys_touch[1]
    print(f"Monkey business: {monkey_business}")


if __name__ == "__main__":
    main()
