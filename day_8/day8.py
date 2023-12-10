import re
import numpy as np
import time
from aocd import get_data

start = time.time()

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

positions = []
position_totals = []

# find start positions
for key in puzzle_map:
    if key.endswith("A"):
        positions.append(key)

# Originally tried the way home via BRUTE FORCE! Reddit tells me this would take 182 days and that LCM is the way 
# This code is mine, but I needed the Reddit tip to find the shortest path to victory

for position in positions:
    num_moves = 0
    lost =  True
    while lost:
        for i in range(len(moves)):
            num_moves += 1
            position = puzzle_map[position][index[moves[i]]]
            if position[-1] == "Z":
                position_totals.append(num_moves)
                lost = False

# find lowest common multiple for the time is takes each position to reach "Z" which is indicative of the number of moves
# it takes for ALL positions to reach "Z"
arr = np.array(position_totals)
x = np.lcm.reduce(arr)

end = time.time()

print(f"Part 2 - Number of Moves: {x}")

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")