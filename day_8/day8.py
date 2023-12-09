import re
from aocd import get_data

puzzle = get_data(day=8, year=2023).splitlines()

# dict to convert moves to index 
index = {
    "L" : 0,
    "R" : 1
}

# moves are the first line
moves = puzzle[0]

# convert input to map
puzzle_map = {}
for line in puzzle[2:]:
    line = re.sub("[^A-Z]", " ", line,0,re.IGNORECASE) 
    line = line.split()
    puzzle_map[line[0]] = [line[1], line[2]]

### PART 1 ###
num_moves = 0
location = "AAA"
lost =  True

while lost:
    for i in range(len(moves)):
        num_moves += 1
        location = puzzle_map[location][index[moves[i]]]
        if location == "ZZZ":
            lost = False

print(f"Part 1 - Number of Moves: {num_moves}")

### PART 2 ###
num_moves = 0
lost =  True
positions = []

# find start positions
for key in puzzle_map:
    if key.endswith("A"):
        positions.append(key)

# find the way home via BRUTE FORCE! 
# This sadly does not seem to work (at least not in a reasonable time) - Reddit indicates I need to be using LCM
while lost:
    for move in range(len(moves)): # iterate over moves. ie. L or R
        positions = list(map( lambda p: puzzle_map[p][index[moves[move]]], positions ))
        num_moves += 1
        correct_positions = 0
        for position in positions: # see how many positions are correct
            if position.endswith("Z"):
                correct_positions += 1
                print(f"FOUND A Z! - {positions}")
                input()
    
        if correct_positions == len(positions): # determine if we have all correct positions!
            lost = False

