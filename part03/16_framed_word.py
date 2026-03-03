# Write your solution here
word = input("Word: ")

print("*"*30)

total_space = 28 - len(word)
left_space = total_space // 2
right_space = total_space - left_space

print("*" + " " * left_space + word + " " * right_space + "*")
print("*"*30)

