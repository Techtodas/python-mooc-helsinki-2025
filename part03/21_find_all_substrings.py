input_string = input("Please type in a word: ")
substring = input("Please type in a character: ")

index = input_string.find(substring)

while index != -1 and index + 3 <= len(input_string):
    print(input_string[index:index+3])
    index = input_string.find(substring, index + 1)
