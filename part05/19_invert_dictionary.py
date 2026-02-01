# Write your solution here
def invert(dictionary: dict):
    inverted_list = {}
    for key, value in dictionary.items():
        inverted_list[value] = key
    dictionary.clear()

    for key, value in inverted_list.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)