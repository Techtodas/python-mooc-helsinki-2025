# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        print("Thanks and bye!")
        break

    result = 1
    tracker = 1
    while tracker <= number:
        result*=tracker
        tracker+=1

    print(f"The factorial of the number {number} is {result}")

