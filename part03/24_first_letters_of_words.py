# Write your solution here
sentence = input("Please type in a sentence:")
counter = 0

while counter < len(sentence):

    if counter == 0:
        print(sentence[0])

    elif sentence[counter - 1] == " ":
        print(sentence[counter])

    counter+=1