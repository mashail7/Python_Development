pokemon_distances = list(map(int, input().split()))
total_removed = 0

while len(pokemon_distances) > 0:
    index = int(input())

    if index < 0:
        removed = pokemon_distances.pop(0)

        if pokemon_distances:
            pokemon_distances.insert(0, pokemon_distances[-1])

    elif index >= len(pokemon_distances):
        removed = pokemon_distances.pop()

        if pokemon_distances:
            pokemon_distances.append(pokemon_distances[0])

    else:
        removed = pokemon_distances.pop(index)

    total_removed += removed

    for i in range(len(pokemon_distances)):
        if pokemon_distances[i] <= removed:
            pokemon_distances[i] += removed
        else:
            pokemon_distances[i] -= removed

print(total_removed)