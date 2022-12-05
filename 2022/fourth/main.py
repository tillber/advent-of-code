assignments = open("assignments.txt", "r").read()


def main():
    subset = 0
    intersection = 0

    for assignment in assignments.split("\n"):
        [a1, a2] = assignment.split(',')

        [a1_min, a1_max] = a1.split('-')
        [a2_min, a2_max] = a2.split('-')

        a1_set = set(range(int(a1_min), int(a1_max) + 1))
        a2_set = set(range(int(a2_min), int(a2_max) + 1))

        if a1_set.issubset(a2_set) or a2_set.issubset(a1_set):
            subset += 1

        if a1_set.intersection(a2_set):
            intersection += 1

    print(subset)
    print(intersection)


if __name__ == "__main__":
    main()
