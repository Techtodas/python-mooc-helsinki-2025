# Write your solution here
contacts = {}

while True:
    ask_user = int(input("command (1 search, 2 add, 3 quit):"))
    if ask_user == 3:
        print("quitting...")
        break

    if ask_user == 1:
        search_name = input("name: ")
        if search_name in contacts:
            print(contacts[search_name])
        else:
            print("no number")

    elif ask_user == 2:
        add_name = input("name: ")
        add_number = input("number: ")
        contacts[0] = add_name
        contacts[add_name] =  add_number
        print("ok!")

            
            