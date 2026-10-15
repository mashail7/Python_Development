business_center_rooms = int(input())
number_of_room = 0
has_enough_chairs = True
total_free_chairs = 0

for room in range(business_center_rooms):
    chair_and_visitors = input().split()
    chairs = chair_and_visitors[0]
    visitors = int(chair_and_visitors[1])
    number_of_room += 1

    if len(chairs) < visitors:
        needed_chairs_in_room = visitors - len(chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
        has_enough_chairs = False
    else:
        total_free_chairs += len(chairs) - visitors


    if room == business_center_rooms - 1 and has_enough_chairs:
        print(f"Game On, {total_free_chairs} free chairs left")