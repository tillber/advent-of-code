# Read calories from file.
calories = open("calories.txt", "r").read()

def main():
    elfs = list(map(lambda elf: list(map(int, elf.split("\n"))), calories.split("\n\n")))
    elfs_calories = list(map(sum, elfs))

    print(f"The elf carrying the most calories carries a total of {max(elfs_calories)} calories!")

    total_cals = sum(sorted(elfs_calories, reverse=True)[:3])
    print(f"The top three elves carrying the most calories are carrying {total_cals} calories in total!")

if __name__ == "__main__":
    main()