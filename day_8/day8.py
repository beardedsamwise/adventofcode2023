import re

# input = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

# input = input.splitlines()

from aocd import get_data
input = get_data(day=8, year=2023).splitlines()

# dict to convert moves to index 
index = {
    "L" : 0,
    "R" : 1
}

# moves are the first 
moves = input[0]

# convert input to map
map = {}
for line in input[2:]:
    line = re.sub("[^A-Z]", " ", line,0,re.IGNORECASE) 
    line = line.split()
    map[line[0]] = [line[1], line[2]]

# process number of moves
num_moves = 0
location = "AAA"
lost =  True

while lost:
    for i in range(len(moves)):
        num_moves += 1
        moving_to = map[location][index[moves[i]]]
        location = moving_to
        if location == "ZZZ":
            lost = False

print(f"Part 1 - Number of Moves: {num_moves}")






