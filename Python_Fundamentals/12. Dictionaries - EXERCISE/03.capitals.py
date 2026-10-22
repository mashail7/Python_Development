countries = input().split(", ")
capitals = input().split(", ")
# final_data = {countries[index]: capitals[index] for index in range(len(countries))}
final_data = dict(zip(countries, capitals))
for country, capital in final_data.items():
    print(f"{country} -> {capital}")