exam_results = {}
submissions = {}

while True:
    line = input()

    if line == "exam finished":
        break

    arguments = line.split("-")

    if arguments[1] == "banned":
        exam_results.pop(arguments[0], None)
        continue

    username = arguments[0]
    language = arguments[1]
    points = int(arguments[2])

    submissions[language] = submissions.get(language, 0) + 1

    if username not in exam_results:
        exam_results[username] = {}

    if language not in exam_results[username]:
        exam_results[username][language] = points
    elif points > exam_results[username][language]:
        exam_results[username][language] = points

print("Results:")

for username, languages in exam_results.items():
    print(f"{username} | {max(languages.values())}")

print("Submissions:")

for language, count in submissions.items():
    print(f"{language} - {count}")