students = {}

while True:
    command = input()

    if ":" not in command:
        searched_course = command.replace("_", " ")
        break

    name, student_id, course = command.split(":")
    students[name] = [student_id, course]

for name, info in students.items():
    student_id = info[0]
    course = info[1]

    if course == searched_course:
        print(f"{name} - {student_id}")