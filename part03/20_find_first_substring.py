# Write your solution here
input_string = input("Please type in a word: ")
substring = input("Please type in a character: ")
index = input_string.find(substring)
if len(input_string[index:]) > 2:
    print(f"{input_string[index:index+3]}")