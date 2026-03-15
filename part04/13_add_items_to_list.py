# Write your solution here
limit = int(input("How many times: "))
item = []
i = 1

while i <= limit:
    add_item = int(input(f"Item {i}: "))
    item.append(add_item)
    i+=1

print(item)