# Write your solution here
number = int(input("Please type in a number: "))
counter = 1

while counter <= number:

    if counter + 1 <= number:
        print(counter+1)
        print(counter)
    else:
        print(counter)

    counter+=2