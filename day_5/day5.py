# load input
from aocd import get_data
input = get_data(day=5, year=2023).splitlines()

# set seeds
seeds = (input[0][7:]).split()

# init empty map and key values
map = {}
key = ""

# convert input to dict
for line in input[2:]:
    if not line: # skip blank lines
        continue
    elif line[0].isalpha(): # set key for dict and remove superfluous text
        key = line.split()[0]
        map[key] = []
    else: # append list to dict 
        map[key].append(line.split()) 

print(map)