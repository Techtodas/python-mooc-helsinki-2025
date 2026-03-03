# Write your solution here
number = int(input("Please type in a number: "))
counter = 1

while counter <= number:
    i = 0
    while i < number:
        i+=1
        print(f"{counter} x {i} = {counter*i}")
    counter+=1
    
    
