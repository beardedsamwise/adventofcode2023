# load input.txt
with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

WIN_CARD_NUM = 5

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
# figure out which cards have wins to tally scores
winning_cards_list = []

total_cards_won = 0

# while loop through all winning cards - if winning card is found append card to winning cards list

for i in range(len(input)):
    winning_cards = card_wins(input[i])
    print(f"cards won: {winning_cards} - card {i + 1}")
    if winning_cards:
        for j in range(i + 1, i + winning_cards + 1):
            winning_cards_list.append(j)
            total_cards_won += 1

print(winning_cards_list)
print(total_cards_won)

while winning_cards_list:
    card = winning_cards_list.pop(0)
    print(f"pop card: {card + 1}")
    winning_cards = card_wins(input[card])
    print(f"cards won: {winning_cards}")
    if winning_cards:
        for j in range(card + 1, card + winning_cards + 1):
            print(f"added card {j + 1}")
            winning_cards_list.append(j)
            total_cards_won += 1
    print(winning_cards_list)

print(total_cards_won)
print(winning_cards_list)