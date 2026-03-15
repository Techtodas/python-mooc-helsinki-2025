# Write your solution here
while True:
    with open("dictionary.txt", "a") as add:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))
        if function == 3:
            print("Bye!")
            break

        if function == 1:
            finnish_word = input("The word in Finnish: ")
            english_word = input("The word in English: ")

            add.write(finnish_word+";")
            add.write(english_word+"\n")
            print("Dictionary entry added")
        
        elif function == 2:
            search = input("Search term: ")

            with open("dictionary.txt") as read:
                for line in read:
                    line = line.strip()
                    parts = line.split(";")

                    if search in parts[0]:
                        print(f"{parts[0]} - {parts[1]}")
                    elif search in parts[1]:
                        print(f"{parts[0]} - {parts[1]}")
            #print(result)
            #print(result)

