path = input().split("\\")
file_and_extension = path[-1]
file_name = file_and_extension.split(".")[0]
extension = file_and_extension.split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")