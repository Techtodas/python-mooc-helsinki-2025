# Write your solution here
print("1 - add an entry, 2 - read entries, 0 - quit")
while True:
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break

    if function == 1:
        with open("diary.txt", "a") as file:
            add = input("Diary entry: ")
            file.write(f"{add}\n")
            print("Diary saved")
    elif function == 2:
        print("Entries:")
        with open("diary.txt", "r") as read:
            for line in read:
                print(line, end="")
        