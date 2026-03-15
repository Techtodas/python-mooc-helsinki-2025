# Write your solution here
number = [1,2,3,4,5]
i = 0

while i < len(number):
    index = int(input("Index: "))

    if index == -1:
        break

    if number[index] in number:
        new_index = int(input("New index: "))
        number[index] = new_index

    
    print(number)

    i+=1