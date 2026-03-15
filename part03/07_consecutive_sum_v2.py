# Write your solution here
limit = int(input("Limit: "))
total = 0
count = 1
sum = ""
while total < limit:
    total+=count
    if sum == "":
        sum = str(count)
    else:
        sum+= f" + {count}"
    count+=1
    
print(f"The consecutive sum: {sum} = {total}")