# Write your solution here
def everything_reversed(my_list):
    reversed_list = []
    for i in my_list:
        reversed_list.append(i[::-1])
    return reversed_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)