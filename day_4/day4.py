# load input
from aocd import get_data
input = get_data(day=4, year=2023).splitlines()

WIN_CARD_NUM = 10

# remove game id from line and split string to list
def split_line(line):
    line = line.split()
    del line[0:2]
    return line

# function to tally card score
def card_score(card):
    winning_cards = card[0:WIN_CARD_NUM]
    my_cards = card[WIN_CARD_NUM + 1:]
    card_score = 0
    for card in my_cards:
        if card in winning_cards and card_score == 0:
            card_score += 1
        elif card in winning_cards:
            card_score = card_score * 2
    return card_score

# function to tally winning cards
def card_wins(card):
    winning_cards = card[0:WIN_CARD_NUM]
    my_cards = card[WIN_CARD_NUM + 1:]
    card_wins = 0
    for card in my_cards:
        if card in winning_cards:
            card_wins += 1
    return card_wins

# convert cards to list of lists 
for i in range(len(input)):
    input[i] = split_line(input[i])

# part 1
# process each line of cards

total_score = 0

for card in input:
    total_score += card_score(card)

print(f"Part 1 - Total Score: {total_score}")

# part 2

winning_cards_list = []
total_cards_won = 0

# process initial winning cards

for i in range(len(input)):
    winning_cards = card_wins(input[i])
    if winning_cards:
        for j in range(i + 1, i + winning_cards + 1):
            winning_cards_list.append(j)
            total_cards_won += 1

# while loop through previous winning cards adding new winning cards as we go 
# this is HIGHLY inefficient and takes a long time to run

while winning_cards_list:
    card = winning_cards_list.pop(0)
    winning_cards = card_wins(input[card])
    if winning_cards:
        for j in range(card + 1, card + winning_cards + 1):
            winning_cards_list.append(j)
            total_cards_won += 1


total_cards_won = total_cards_won + len(input)

print(f"Part 2 - Total Cards Won - {total_cards_won}")