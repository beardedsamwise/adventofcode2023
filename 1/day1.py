import re

### PART 1 ###
with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

calibration_values = []

# loop through each line, remove any non numeric characters then construct calibration value
for line in input:
    values = re.sub("[^0-9]", "", line)
    calibration_values.append(int(values[0] + values[-1]))   

# sum the values! 
part_1_result = sum(calibration_values)
print(f"Part 1 - Calibration Value Sum: {part_1_result}")

### PART 2 ###

calibration_values = []

conversion_table = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

# take a line from the input file and extract all numbers (either numeric or alphanumeric)
def clean_string(line):
    results = []
    for i in range(len(line)):
        if line[i].isnumeric():
            results.append(line[i])
        else: # loop through keys in conversion table to look for alphanumeric numbers at start of string
            line_search = line[i:]
            for key in conversion_table:
                if line_search.startswith(key):
                    results.append(str(conversion_table.get(key)))
    return results

for line in input:
    line = clean_string(line)
    calibration_values.append(int(str(line[0]) + str(line[-1])))  

part_2_result = sum(calibration_values)

print(f"Part 2 - Calibration Value Sum: {part_2_result}")