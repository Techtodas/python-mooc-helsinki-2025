# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    counter = 0
    for i in range(len(my_matrix)):
        for e in range(len(my_matrix[i])):
            if my_matrix[i][e] == element:
                counter+=1

    return counter

if __name__ == "__main__":
    m = [[1, 2, 3], [2, 1, 1], [4, 5, 6]]
    print(count_matching_elements(m, 1))