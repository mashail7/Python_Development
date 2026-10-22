n = int(input())
good_students = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in good_students:
        good_students[student] = [grade]
    elif student  in good_students:
        good_students[student].append(grade)

for student, grades in good_students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")