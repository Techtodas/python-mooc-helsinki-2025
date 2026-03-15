# Write your solution here
def shortest(my_list):
    minimum = []
    min_word = ""

    for i in my_list:
        minimum.append(len(i))
        if min(minimum) == len(i):
            min_word = i
    return min_word

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)