# Write your solution here
word = input("Please type in a string: ")
counter = 0
reverse = -1
while counter < len(word):
    print(word[reverse])
    counter+=1
    reverse-=1
    