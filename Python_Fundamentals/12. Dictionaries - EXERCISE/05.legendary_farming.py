key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk_materials = {}

while True:
    data = input().split()

    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                key_materials[material] -= 250

                if material == "shards":
                    legendary_item = "Shadowmourne"
                elif material == "fragments":
                    legendary_item = "Valanyr"
                else:
                    legendary_item = "Dragonwrath"

                print(f"{legendary_item} obtained!")
                break
        else:
            junk_materials[material] = (
                junk_materials.get(material, 0) + quantity
            )
    else:
        continue

    break

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")