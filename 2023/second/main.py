from functools import reduce
from operator import mul


games_input = open("games.txt", "r").read()
games = games_input.split("\n")

cube_input = {"red": 12, "green": 13, "blue": 14}
print(f"cube input: {cube_input}")

possible_games = set()
possible_games_color_maps = {}

for game in games:
    game_parts = game.split(":")

    id_str = game_parts[0]
    id = int(id_str.split(" ")[1])
    print(id_str)

    possible_games.add(id)

    rounds = game_parts[1].split(";")
    cubes = [cube.strip() for round in rounds for cube in round.split(",")]

    color_map = {}

    for cube in cubes:
        cube_parts = cube.split(" ")
        color = cube_parts[1]
        amount = int(cube_parts[0])

        # find max amount of cubes
        color_map[color] = max(amount, color_map.get(color, 0))

    possible_games_color_maps[id] = list(color_map.values())

    # for color in color_map.keys():
    #     print(f"{color}: input; {cube_input[color]}, found; {color_map[color]}")

    #     if cube_input[color] < color_map[color] and id in possible_games:
    #         possible_games.remove(id)

    print(color_map)

    print(f"is possible: {id in possible_games}")

print(
    sum(
        [
            reduce(lambda x, y: x * y, entry[1])
            for entry in possible_games_color_maps.items()
            if entry[0] in possible_games
        ]
    )
)

# print(sum(possible_games))
