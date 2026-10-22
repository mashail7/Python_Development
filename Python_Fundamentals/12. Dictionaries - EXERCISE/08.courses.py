course_and_students = {}

while True:
    command = input()
    if command == "end":
        break

    course, student = command.split(" : ")

    if course not in course_and_students:
        course_and_students[course] = []
    course_and_students[course].append(student)

for course, students in course_and_students.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")