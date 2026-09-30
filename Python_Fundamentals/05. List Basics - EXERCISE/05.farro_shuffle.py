deck = input().split()
count_of_shuffles = int(input())
shuffled_deck = []

for i in range(count_of_shuffles):
    shuffled_deck = []

    for j in range(len(deck) // 2):
        first_half = deck[0:len(deck) // 2:]
        second_half = deck[len(deck) // 2:]

        shuffled_deck.append(first_half[j])
        shuffled_deck.append(second_half[j])

    deck = shuffled_deck

print(shuffled_deck)