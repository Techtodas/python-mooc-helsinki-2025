# write your solution here
user_input = input("Write text: ")

with open("wordlist.txt") as new_file:
    data = []
    
    for line in new_file:
        line = line.strip()
        data.append(line)
    
    for word in user_input.split():
        if word.lower() not in data:
            print(f"*{word}* ", end="")
        else:
            print(f"{word}", end=" ")