price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()

entry_value = price_ratings[entry_point]
left_part = price_ratings[:entry_point]
right_part = price_ratings[entry_point + 1:]

if type_of_items == "cheap":
    left_damage = sum(x for x in left_part if x < entry_value)
    right_damage = sum(x for x in right_part if x < entry_value)
elif type_of_items == "expensive":
    left_damage = sum(x for x in left_part if x >= entry_value)
    right_damage = sum(x for x in right_part if x >= entry_value)

if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")