forrest = open("forrest.txt", "r").read()

trees = list(map(lambda x: list(x), forrest.split("\n")))


def main():
    visible_trees = (len(trees[0]) + (len(trees) - 2)) * 2

    for i in range(1, (len(trees) - 1)):
        for j in range(1, (len(trees[i]) - 1)):
            calculate_scenic_score(i, j)
            if is_visible(i, j):
                visible_trees += 1

    print(f"Number of visible trees: {visible_trees}")


def is_visible(y, x) -> bool:
    tree = trees[y][x]

    hidden_left = False
    for k in range(x, 0, -1):  # left
        if trees[y][k - 1] >= tree:
            hidden_left = True
            break

    hidden_right = False
    for k in range(x, len(trees[y]) - 1, 1):  # right
        if trees[y][k + 1] >= tree:
            hidden_right = True
            break

    hidden_top = False
    for k in range(y, 0, -1):  # top
        if trees[k - 1][x] >= tree:
            hidden_top = True
            break

    hidden_bottom = False
    for k in range(y, len(trees) - 1, 1):  # bottom
        if trees[k + 1][x] >= tree:
            hidden_bottom = True
            break

    return not (hidden_right and hidden_left and hidden_top and hidden_bottom)


def calculate_scenic_score(y, x) -> bool:
    tree = trees[y][x]
    scenic_factors = []

    hidden_left = False
    for k in range(x, 0, -1):  # left
        if trees[y][k - 1] >= tree:
            distance = x - (k - 1)
            scenic_factors.append(distance)
            break

    hidden_right = False
    for k in range(x, len(trees[y]) - 1, 1):  # right
        if trees[y][k + 1] >= tree:
            distance = x - (k + 1)
            scenic_factors.append(distance)
            break

    hidden_top = False
    for k in range(y, 0, -1):  # top
        if trees[k - 1][x] >= tree:
            distance = y - (k - 1)
            scenic_factors.append(distance)
            break

    hidden_bottom = False
    for k in range(y, len(trees) - 1, 1):  # bottom
        if trees[k + 1][x] >= tree:
            distance = y - (k + 1)
            scenic_factors.append(distance)
            break

    print(scenic_factors)
    return not (hidden_right and hidden_left and hidden_top and hidden_bottom)


if __name__ == "__main__":
    main()
