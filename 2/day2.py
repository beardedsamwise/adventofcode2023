import re

### PART 1 ###
with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

max_cubes = {
    "red" : 12,
    "green": 13,
    "blue" : 14
}

def split_line(line):
    line = line.split()
    del line[0:2]
    return line

def convert_game_max(line):
    game = {
    "red" : 0,
    "green": 0,
    "blue" : 0
    }
    line = split_line(line)
    for i in range(0, len(line), 2):
        colour = line[i + 1]
        colour = re.sub("[^a-zA-Z]", "", colour)
        number = int(line[i])
        if int(game[colour]) < int(number):
            game[colour] = number
    return game

games = {}

for i in range(len(input)):
    games[i + 1] = convert_game_max(input[i])

sum = 0

for game,cubes in games.items():
    if (max_cubes["blue"] >= cubes["blue"]) and (max_cubes["red"] >= cubes["red"]) and (max_cubes["green"] >= cubes["green"]):
        sum += game

print(f"Part 1 - Sum - {sum}")

### PART 2 ###

sum = 0

for game,cubes in games.items():
    sum += cubes["red"] * cubes["blue"] * cubes["green"]

print(f"Part 2 - Sum - {sum}")