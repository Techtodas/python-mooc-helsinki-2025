# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
counter = 0

while counter < height:
    print("#"*(height+width-height))
    counter+=1