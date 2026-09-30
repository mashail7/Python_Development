input_list = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells_put_out = []

for fire in input_list:
    fire_type, fire_range = fire.split(" = ")
    fire_range = int(fire_range)
    if fire_type == "High" and 81 <= fire_range <= 125:
        if water >= fire_range:
            water -= fire_range
            cells_put_out.append(fire_range)
            effort += fire_range * 0.25
            total_fire += fire_range
    elif fire_type == "Medium" and 51 <= fire_range <= 80:
        if water >= fire_range:
            water -= fire_range
            cells_put_out.append(fire_range)
            effort += fire_range * 0.25
            total_fire += fire_range
    elif fire_type == "Low" and 1 <= fire_range <= 50:
        if water >= fire_range:
            water -= fire_range
            cells_put_out.append(fire_range)
            effort += fire_range * 0.25
            total_fire += fire_range

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")