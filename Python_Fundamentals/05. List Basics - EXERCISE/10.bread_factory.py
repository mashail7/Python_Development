events_list = input().split("|")
energy = 100
coins = 100
is_day_completed = True

for event in events_list:
    event_or_ingredient, number = event.split("-")

    if event_or_ingredient == "rest":
       previous_energy = energy
       energy = min(100, energy + int(number))
       gained_energy = energy - previous_energy
       print(f"You gained {gained_energy} energy.")
       print(f"Current energy: {energy}.")
    elif event_or_ingredient == "order":
        if energy >= 30:
            coins += int(number)
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy = min(100, energy + 50)
            print("You had to rest!")
    else:
        if coins >= int(number):
            coins -= int(number)
            print(f"You bought {event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            is_day_completed = False
            break

if is_day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")