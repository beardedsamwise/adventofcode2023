import re

# input = """"""
# input = input.splitlines()

from aocd import get_data
input = get_data(day=8, year=2023).splitlines()

# dict to convert moves to index 
index = {
    "L" : 0,
    "R" : 1
}

# moves are the first line
moves = input[0]

# convert input to map
map = {}
for line in input[2:]:
    line = re.sub("[^A-Z]", " ", line,0,re.IGNORECASE) 
    line = line.split()
    map[line[0]] = [line[1], line[2]]

### PART 1 ###
# process number of moves
# num_moves = 0
# location = "AAA"
# lost =  True

# while lost:
#     for i in range(len(moves)):
#         num_moves += 1
#         location = map[location][index[moves[i]]]
#         if location == "ZZZ":
#             lost = False

# print(f"Part 1 - Number of Moves: {num_moves}")

### PART 2 ###
num_moves = 0
# pos_1 = "11A"
# pos_2 = "22A"
lost =  True
positions = []

print(map)

for key in map:
    print(key)
    if key.endswith("A"):
        positions.append(key)

print(positions)

while lost:
    for move in range(len(moves)): # iterate over moves. ie. L or R
        for position in range(len(positions)): # iterate over each position (ie. make multiple moves simaltaneously)
            # print(move) # 0
            # print(position) # AAA
            positions[position] = map[positions[position]][index[moves[move]]]
        num_moves += 1
        correct_positions = 0
        for position in positions:
            if position.endswith("Z"):
                correct_positions += 1
        print(positions)
        if correct_positions == len(positions):
            lost = False

print(f"Part 2 - Number of Moves: {num_moves}")

