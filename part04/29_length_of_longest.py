# Write your solution here
def length_of_longest(my_list: list):
    best = []
    for i in my_list:
        best.append(len(i))
    return max(best)
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)