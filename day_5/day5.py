# load input.txt
with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

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