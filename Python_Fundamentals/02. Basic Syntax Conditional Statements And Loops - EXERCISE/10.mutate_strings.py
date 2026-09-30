first_string = input()
second_string = input()
index_to_end = 1
previous_string = first_string

while index_to_end <= len(first_string):
    third_string = ""

    for i in range(len(first_string)):
        if i == index_to_end - 1:
            third_string += second_string[i]
        else:
            third_string += previous_string[i]

    if third_string != previous_string:
        print(third_string)

    previous_string = third_string
    index_to_end += 1