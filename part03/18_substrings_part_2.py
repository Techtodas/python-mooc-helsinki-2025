# Write your solution here
word = input("Please type in a string: ")
counter = 0

while counter < len(word):
    counter+=1
    print(word[-counter:])