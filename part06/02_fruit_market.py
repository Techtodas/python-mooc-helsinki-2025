# write your solution here
def read_fruits():
    fruits = {}

    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])

    return fruits

if __name__ == "__main__":
    print(read_fruits())