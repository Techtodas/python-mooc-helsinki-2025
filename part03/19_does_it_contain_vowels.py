# Write your solution here
input_string = input("Please type in a string: ")
vowels = "aeo"
counter = 0

while counter < len(vowels):
    if vowels[counter] in input_string:
        print(f"{vowels[counter]} found")
    else:
        print(f"{vowels[counter]} not found")

    counter+=1