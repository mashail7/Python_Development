strings = input().split()
final_string = ""

for string in strings:
    repeat_times = len(string)
    final_string += string * repeat_times

print(final_string)