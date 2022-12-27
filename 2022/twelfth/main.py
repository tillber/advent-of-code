heights = open("heights.txt", "r").read()


def is_valid_step(matrix, visited, curr_pos, new_pos):
    new_pos_y, new_pos_x = new_pos
    curr_pos_y, curr_pos_x = curr_pos

    # in range of matrix
    in_range = new_pos_y >= 0 and new_pos_y < len(
        matrix) and new_pos_x >= 0 and new_pos_x < len(matrix[0])

    if not in_range:
        return False

    # is visited previously
    is_visited = visited[new_pos_y][new_pos_x]

    if is_visited:
        return False

    # is step possible (elevation)
    elev_new = ord(matrix[new_pos_y][new_pos_x])
    elev_curr = ord(matrix[curr_pos_y][curr_pos_x])

    is_possible_step = elev_new <= elev_curr + 1

    if not is_possible_step:
        return False

    return True


class Node:
    def __init__(self, y, x, dist):
        self.y = y
        self.x = x
        self.dist = dist


def find_shortest_path(matrix, start, goal):  # bfs
    queue = []
    visited = [[False for _ in range(len(matrix[0]))]
               for _ in range(len(matrix))]

    start = Node(start[0], start[1], 0)

    queue.append(start)
    visited[start.y][start.x] = True

    while len(queue) > 0:
        curr = queue.pop(0)

        if (curr.y, curr.x) == goal:
            return curr.dist  # goal reached

        # adjacent nodes
        adjacent = ((curr.y + 1, curr.x), (curr.y, curr.x + 1),
                    (curr.y - 1, curr.x), (curr.y, curr.x - 1))

        for (y, x) in adjacent:
            if is_valid_step(matrix, visited, (curr.y, curr.x), (y, x)):
                queue.append(Node(y, x, curr.dist + 1))
                visited[y][x] = True


def main():
    grid = list(map(list, heights.split("\n")))

    start = find_pos(grid, "S")
    goal = find_pos(grid, "E")

    grid[start[0]][start[1]] = 'a'  # "S" equates to "a"
    grid[goal[0]][goal[1]] = 'z'  # "E" equates to "z"

    print(f"Start coordinates: {start}")
    print(f"Goal coordinates: {goal}")

    dist = find_shortest_path(grid, start, goal)
    print(f"Shortest path distance from S to E: {dist} steps")

    start_nodes = find_pos(grid, "a")
    dists = list(map(lambda start_node: find_shortest_path(
        grid, start_node, goal), start_nodes))´

    print(
        f"Shortest path distance from any starting position ('a') to E: {min(dists)} steps"
    )


def find_pos(grid, char):
    nodes = []

    for y, row in enumerate(grid):
        try:
            x = row.index(char)
            nodes.append((y, x))
        except ValueError:
            pass

    if len(nodes) == 1:
        return nodes[0]

    return nodes


if __name__ == "__main__":
    main()
