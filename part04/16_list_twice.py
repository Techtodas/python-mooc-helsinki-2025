# Write your solution here
number = []

while True:
    input_number = int(input("New item: "))
    number.append(input_number)

    if input_number == 0:
        print("Bye!")
        break

    print(f"The list now: {number}")
    print(f"The list in order: {sorted(number)}")