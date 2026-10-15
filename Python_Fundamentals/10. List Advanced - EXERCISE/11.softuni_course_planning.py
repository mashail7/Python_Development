schedule = input().split(", ")

while True:
    command = input()

    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        lesson = parts[1]

        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        lesson = parts[1]
        index = int(parts[2])

        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif action == "Remove":
        lesson = parts[1]

        if lesson in schedule:
            schedule.remove(lesson)

            exercise = lesson + "-Exercise"
            if exercise in schedule:
                schedule.remove(exercise)

    elif action == "Swap":
        lesson1 = parts[1]
        lesson2 = parts[2]

        if lesson1 in schedule and lesson2 in schedule:
            index1 = schedule.index(lesson1)
            index2 = schedule.index(lesson2)

            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]

            exercise1 = lesson1 + "-Exercise"
            exercise2 = lesson2 + "-Exercise"

            if exercise1 in schedule:
                schedule.remove(exercise1)
                schedule.insert(schedule.index(lesson1) + 1, exercise1)

            if exercise2 in schedule:
                schedule.remove(exercise2)
                schedule.insert(schedule.index(lesson2) + 1, exercise2)

    elif action == "Exercise":
        lesson = parts[1]
        exercise = lesson + "-Exercise"

        if lesson in schedule:
            if exercise not in schedule:
                schedule.insert(schedule.index(lesson) + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

for index, lesson in enumerate(schedule, start=1):
    print(f"{index}.{lesson}")