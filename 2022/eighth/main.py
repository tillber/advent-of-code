from typing import Tuple
from functools import reduce


forrest = open("forrest.txt", "r").read()
trees = list(map(lambda x: list(x), forrest.split("\n")))


def main():
    scenic_scores = []
    visible_trees = (len(trees[0]) + (len(trees) - 2)) * 2

    for i in range(1, (len(trees) - 1)):
        for j in range(1, (len(trees[i]) - 1)):
            visible, scenic_score = is_visible(i, j)

            if visible:
                visible_trees += 1

            scenic_scores.append(scenic_score)

    print(f"Number of visible trees: {visible_trees}")
    print(f"Highest scenic score: {max(scenic_scores)}")


def is_visible(y, x) -> Tuple[bool, int]:
    tree = trees[y][x]
    scenic_factors = []

    hidden_left = False
    for k in range(x, 0, -1):  # left
        is_higher = trees[y][k - 1] >= tree
        at_edge = (k-1) == 0

        if is_higher or at_edge:
            distance = abs(x - (k - 1))
            scenic_factors.append(distance)

            if is_higher:
                hidden_left = True
                break

    hidden_right = False
    for k in range(x, len(trees[y]) - 1, 1):  # right
        is_higher = trees[y][k+1] >= tree
        at_edge = (k+1) == len(trees[y]) - 1

        if is_higher or at_edge:
            distance = abs(x-(k + 1))
            scenic_factors.append(distance)

            if is_higher:
                hidden_right = True
                break

    hidden_top = False
    for k in range(y, 0, -1):  # top
        is_higher = trees[k-1][x] >= tree
        at_edge = (k-1) == 0

        if is_higher or at_edge:
            distance = abs(y-(k-1))
            scenic_factors.append(distance)

            if is_higher:
                hidden_top = True
                break

    hidden_bottom = False
    for k in range(y, len(trees) - 1, 1):  # bottom
        is_higher = trees[k+1][x] >= tree
        at_edge = (k+1) == len(trees) - 1

        if is_higher or at_edge:
            distance = abs(y-(k+1))
            scenic_factors.append(distance)

            if is_higher:
                hidden_bottom = True
                break

    scenic_score = reduce((lambda x, y: x*y), scenic_factors)
    visible = not (
        hidden_right and hidden_left and hidden_top and hidden_bottom
    )

    return visible, scenic_score


if __name__ == "__main__":
    main()
