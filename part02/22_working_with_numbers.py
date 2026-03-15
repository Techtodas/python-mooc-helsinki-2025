# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
summ = 0
sum_of_numbers = 0
positive_number = 0
negative_number = 0

while True:
    number = int(input("Number:"))
    
    if number == 0:
        # Counting the numbers.
        print("Numbers typed in", count)

        # Sum of the typed numbers.
        print("The sum of the numbers is", sum_of_numbers)

        # Sum of the typed numbers.
        print("The mean of the numbers is", mean)

        print("Positive numbers", positive_number)
        print("Negative numbers", negative_number)
        break

    # Counting the postive and negative numbers.
    if number > 0:
        positive_number+=1
    else:
        negative_number+=1
    
    count += 1
    number+=sum_of_numbers
    sum_of_numbers = number
    mean = (sum_of_numbers)/count
    
    
    print("sum", sum_of_numbers)
    print("mean", mean)
    print("count", count)

