box = []
i = 1
while True:
    print(f"The list is now {box}")
    user_input = input("a(d)d, (r)emove or e(x)it:")

    if user_input == "d":
        box.append(i)
        i+=1
        
    if user_input == "r":
        box.pop()
        if len(box) == 0:
            i=1
        else:
            i=i-1

    if user_input == "x":
        print("Bye!")
        break