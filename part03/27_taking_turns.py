# Write your solution here
number = int(input("Please type in a number: ")) # --> 5 4 3
counter = 1 # --> 2 3 4

while counter <= number:

    if counter + 1 <= number:
        print(counter)
        print(number)
    else:
        print(counter)

    counter+=1
    number-=1
