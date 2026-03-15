# Write your solution here
inscribe = input("Whom should I sign this to: ")
filename = input("Where shall I save it: ")

with open(filename, "w") as my_file:
    my_file.write(f"Hi {inscribe},")
    my_file.write(f" we hope you enjoy learning Python with us!")
    my_file.write(f" Best, Mooc.fi Team")


