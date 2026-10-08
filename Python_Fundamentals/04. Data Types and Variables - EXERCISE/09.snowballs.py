n = int(input())
highest_snowball = 0
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for i in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball = (snowball_weight // snowball_time) ** snowball_quality
    if snowball > highest_snowball:
        highest_snowball = snowball
        highest_snowball_weight = snowball_weight
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality

print(f"{highest_snowball_weight} : {highest_snowball_time} = {highest_snowball} ({highest_snowball_quality})")