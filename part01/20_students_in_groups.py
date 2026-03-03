# Write your solution here
number1 = int(input("How many students on the course?"))
number2 = int(input("Desired group size?"))

q = number1//number2

if number1%number2 != 0:
    q+=1

print(f"Number of groups formed: {q}")