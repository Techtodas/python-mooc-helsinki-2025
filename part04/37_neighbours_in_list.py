# Write your solution here
def longest_series_of_neighbours(my_list):
    current_lenght = 1
    longest_lenght = 1

    for i in range(len(my_list) - 1):
        current = my_list[i]
        next_element = my_list[i + 1]

        diff = current - next_element

        if diff == 1 or diff == -1:
            current_lenght+=1

            if current_lenght > longest_lenght:
                longest_lenght = current_lenght
        else:
            current_lenght = 1

    return longest_lenght

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))