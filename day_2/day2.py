import re

from aocd import get_data
input = get_data(day=2, year=2023).splitlines()

### PART 1 ###

max_cubes = {
    "red" : 12,
    "green": 13,
    "blue" : 14
}

# remove game id from line
def split_line(line):
    line = line.split()
    del line[0:2]
    return line

# convert game line to dict with the max values for each colour
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

# process all lines in the input (ie. convert them to dict of dict)
for i in range(len(input)):
    games[i + 1] = convert_game_max(input[i])

sum = 0

# tally which games are possible based on max_cubes
for game,cubes in games.items():
    if (max_cubes["blue"] >= cubes["blue"]) and (max_cubes["red"] >= cubes["red"]) and (max_cubes["green"] >= cubes["green"]):
        sum += game

print(f"Part 1 - Sum - {sum}")

### PART 2 ###

sum = 0

# tally score of each game
for game,cubes in games.items():
    sum += cubes["red"] * cubes["blue"] * cubes["green"]

print(f"Part 2 - Sum - {sum}")