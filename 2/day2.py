import re

### PART 1 ###
with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

def split_line(line):
    line = line.split()
    del line[0:2]
    return line

def create_dict_from_input(line):
    game = {}
    line = split_line(line)
    for i in range(0, len(line), 2):
        colour = line[i + 1]
        colour = re.sub("[^a-zA-Z]", "", colour)
        number = line [i]
        if colour not in games:
            games[colour] = number
        if games[colour] < number:
            games[colour] = number
    return game



games = {}

for i in range(len(input)):
    game = create_dict_from_input(input[i])
    print(game)

# print(games)

# games = create_dict_from_input(input)
# print(games)