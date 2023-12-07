import re
import numpy 

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

SPECIAL_CHARACTERS = "!@#$%^&*()-+?_=,<>/"

def search_left(row, column, matrix):
    found_number = None

    for i in range(1,4):
        number = ''.join(matrix[row][column - i : column])
        # print(number)
        if number.isnumeric():
            found_number = int(number)

    if found_number != None:
        return found_number
    else:
        pass       

def search_right(row, column, matrix):
    found_number = None

    for i in range(2,5):
        number = ''.join(matrix[row][column + 1 : column + i])
        if number.isnumeric():
            found_number = int(number)

    if found_number != None:
        return found_number
    else:
        pass   
    
# This is the hottest mess I've ever had the honour of creating 
# BEWARE
# HERE BE CHAOS
def search_above_below(row, column, matrix):
    found_number = []
    if row == 0:
        row = [row + 1]
    elif row == len(matrix) - 1:
        row = [row - 1]
    else:
        row = [row - 1, row + 1]
    for each in row:
        if matrix[each][column].isnumeric():
            centre = search_right(each, column - 2, matrix)
            right = search_right(each, column - 1, matrix)
            left = search_left(each, column + 1, matrix)
            if centre and centre > left:
                found_number.append(centre)
            elif right > left:
                found_number.append(right)
            else:
                found_number.append(left)
        # search shifted one space to right and left
        else:
            shifted_right = search_right(each, column, matrix)
            shifted_left = search_left(each, column, matrix)
            if shifted_left:
                found_number.append(shifted_left)
            if shifted_right:
                found_number.append(shifted_right)

    return found_number

# create schematic as a list of lists (a matrix)
schematic_matrix = []

for i in range(len(input)):
    schematic_matrix.append([])
    for char in input[i]:
        schematic_matrix[i].append(char)

# create list of lists with row, column co-ordinates of symbols

symbol_coords = []

for row in range(len(schematic_matrix)):
    for column in range(len(schematic_matrix[row])):
        if schematic_matrix[row][column] in SPECIAL_CHARACTERS:
            # print(schematic_matrix[row][column])
            symbol_coords.append([row, column])

# calculate results
results = []

for coord in symbol_coords:
    if search_left(coord[0], coord[1], schematic_matrix):
        results.append(search_left(coord[0], coord[1], schematic_matrix))
    if search_right(coord[0], coord[1], schematic_matrix):
        results.append(search_right(coord[0], coord[1], schematic_matrix))
    if search_above_below(coord[0], coord[1], schematic_matrix):
        for each in search_above_below(coord[0], coord[1], schematic_matrix):
            results.append(each)

print(f"Part 1 - {sum(results)}")

 ### PART 2 ###

SPECIAL_CHARACTERS = "*"

gear_coords = []

for row in range(len(schematic_matrix)):
    for column in range(len(schematic_matrix[row])):
        if schematic_matrix[row][column] in SPECIAL_CHARACTERS:
            # print(schematic_matrix[row][column])
            gear_coords.append([row, column])

gear_ratios = []

for coord in gear_coords:
    gears = []
    if search_left(coord[0], coord[1], schematic_matrix):
        gears.append(search_left(coord[0], coord[1], schematic_matrix))
    if search_right(coord[0], coord[1], schematic_matrix):
        gears.append(search_right(coord[0], coord[1], schematic_matrix))
    if search_above_below(coord[0], coord[1], schematic_matrix):
        for each in search_above_below(coord[0], coord[1], schematic_matrix):
            gears.append(each)
    if len(gears) > 1:
        gear_ratios.append(numpy.prod(gears))

print(f"Part 2 - {sum(gear_ratios)}")
