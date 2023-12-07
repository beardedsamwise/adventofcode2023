import numpy 

from aocd import get_data
input = get_data(day=6, year=2023).splitlines()

### PART 1 ###

# remove names from line and split string to list
def split_line(line):
    line = line.split()
    del line[0:1]
    return line

# convert races to list of lists 
for i in range(len(input)):
    input[i] = split_line(input[i])

# calculate how far we can go
distances = []

for i in range(len(input[0])):
    distance = []
    time = int(input[0][i])
    for t in range(time + 1):
        distance.append(t * (time - t))
    distances.append(distance)

# calculate number of ways we can beat record
ways_we_win = []

for i in range(len(distances)):
    wins = 0
    while distances[i]:
        distance = distances[i].pop(0)
        if distance > int(input[1][i]):
            wins += 1
    ways_we_win.append(wins)

print(f"Part 1 - {numpy.prod(ways_we_win)}")

### PART 2 ###

time = int(''.join(input[0]))
record = int(''.join(input[1]))

# calculate how far we can go
distances = []

for t in range(time + 1):
    if (t * (time - t)) > record:
        distances.append(t * (time - t))

print(f"Part 2 - {len(distances)}")
