words_list = input().split()
palindrome = input()

palindrome_list = [word for word in words_list if word[::-1] == word]

print(palindrome_list)

count = palindrome_list.count(palindrome)
print(f"Found palindrome {count} times")