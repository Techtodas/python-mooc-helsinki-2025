# write your solution here
def read_martix():
    data = []

    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            data.append(parts)
    return data

def matrix_sum():
    numbers = read_martix()
    sum_no = []

    for line in numbers:
        for index in line:
            sum_no.append(int(index))
    return sum(sum_no)

def matrix_max():
    numbers = read_martix()
    max_no = []

    for line in numbers:
        for index in line:
            max_no.append(int(index))
    return max(max_no)

def row_sums():
    numbers = read_martix()
    sums = []

    for line in numbers:
        for index in range(len(line)):
            line[index] = int(line[index])
        sums.append(sum(line))
    return sums
