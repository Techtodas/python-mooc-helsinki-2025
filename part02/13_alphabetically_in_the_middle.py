# Write your solution here
a1 = input("1st letter:")
b2 = input("2nd letter:")
c3 = input("3rd letter:")

a = a1.lower()
b = b2.lower()
c = c3.lower()

if a >= b and a <= c or a <= b and a >= c:
    middle = a1
elif b >= a and b <= c or b <= a and b >= c:
    middle = b2
else:
    middle = c3


print(f"The letter in the middle is {middle}")