packing = open("packing.txt", "r").read()


def get_item_prio(char):
    return (ord(char) - 38) if char.isupper() else (ord(char) - 96)


def main():
    rucksacks = packing.split("\n")

    prio = 0
    for rucksack in rucksacks:
        half = len(rucksack)//2
        item = list(set(rucksack[half:]).intersection(set(rucksack[:half])))[0]
        prio += get_item_prio(item)

    print(prio)

    prio = 0
    for i in range(0, len(rucksacks), 3):
        item = list(set(rucksacks[i]).intersection(
            set(rucksacks[i+1])).intersection(set(rucksacks[i+2])))[0]
        prio += get_item_prio(item)

    print(prio)


if __name__ == "__main__":
    main()
