heroes = {}

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split()
    hero_name = tokens[1]
    if tokens[0] == "Enroll":
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []
    elif tokens[0] == "Learn":
        spell_name = tokens[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)
    elif tokens[0] == "Unlearn":
        spell_name = tokens[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

print("Heroes:")
for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")