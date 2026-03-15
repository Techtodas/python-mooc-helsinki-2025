# Write your solution here
def distinct_numbers(my_list: list):
    # This is the solution I create after checking stackoverflow
    #new_list = set(my_list)
    #return sorted(list(new_list))

    # I think this chapter wants me to test what I've learned so far.
    # So I'm gonna use what I know so far.
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return sorted(new_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]