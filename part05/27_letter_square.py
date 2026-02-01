# Write your solution here
layers = int(input("Layers: "))
output = layers * 2 - 1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for r in range(output):
    for c in range(output):
        top = r
        left = c
        bottom = output - 1 - r
        right = output - 1 - c
        layer = min(top, left, bottom, right)

        index = layers - layer - 1
        print(letters[index], end="")
    print()
    