# load input.txt
with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

# remove game id from line and split string to list
def split_line(line):
    line = line.split()
    del line[0:2]
    return line

for i in range(len(input)):
    input[i] = split_line(input[i])

total_score = 0

# process each line of cards
for line in input:
    winning_cards = line[0:10]
    my_cards = line[11:]
    card_score = 0
    for card in my_cards:
        if card in winning_cards and card_score == 0:
            card_score += 1
        elif card in winning_cards:
            card_score = card_score * 2
    total_score += card_score

print(f"Part 1 - Total Score: {total_score}")

