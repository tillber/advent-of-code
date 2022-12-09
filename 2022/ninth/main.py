
import math


moves = open("moves.txt", "r").read()


def main():
    head_y, head_x = 4, 0
    p_head_y, p_head_x = head_y, head_x

    tail_y, tail_x = head_y, head_x  # tail starts at same position as head
    tail_visited = {(tail_y, tail_x)}

    for move in moves.split("\n"):
        dir, amount = tuple(move.split(" "))

        for _ in range(1, int(amount) + 1):
            # copy head's current position (before move)
            p_head_y, p_head_x = head_y, head_x

            if dir == "R":
                head_x += 1
            elif dir == "L":
                head_x -= 1
            elif dir == "U":
                head_y -= 1
            elif dir == "D":
                head_y += 1

            if not (head_y, head_x) in get_adjacent_elements(tail_y, tail_x):
                # move tail
                tail_y = p_head_y
                tail_x = p_head_x

                if not (tail_y, tail_x) in tail_visited:
                    tail_visited.add((tail_y, tail_x))

    print(len(tail_visited))

    return


def get_adjacent_elements(y, x):
    adjacent_elements = set()

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            adjacent_elements.add((y + i, x + j))

    return adjacent_elements


if __name__ == "__main__":
    main()
