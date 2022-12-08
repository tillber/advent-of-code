forrest = open("forrest.txt", "r").read()
trees = list(map(lambda x: list(x), forrest.split("\n")))


def main():
    print(trees)

    visible_trees = (len(trees[0]) + (len(trees) - 2)) * 2

    for i in range(1, (len(trees) - 1)):
        for j in range(1, (len(trees[i]) - 1)):
            if is_visible(i, j):
                visible_trees += 1

    print(visible_trees)


def is_visible(y, x) -> bool:
    tree = trees[y][x]
    print(tree)

    hidden = True
    for k in range(x, 0, -1):  # left
        tr = trees[y][k - 1]
        p_tr = trees[y][k]
        if tr >= p_tr:
            print(tr)
            hidden = True
            print("hidden left")
            break

    for k in range(x, len(trees[y]) - 1, 1):  # right
        tr = trees[y][k + 1]
        p_tr = trees[y][k]
        if tr >= p_tr:
            hidden = True
            print("hidden right")
            break

    for k in range(y, 0, -1):  # top
        tr = trees[k - 1][x]
        p_tr = trees[k][x]
        if tr >= p_tr:
            hidden = True
            print("hidden top")
            break

    for k in range(y, len(trees) - 1, 1):  # bottom
        tr = trees[k + 1][x]
        p_tr = trees[k][x]
        if tr >= p_tr:
            hidden = True
            print("hidden bottom")
            break

    return not hidden


if __name__ == "__main__":
    main()
