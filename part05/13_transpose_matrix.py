# Write your solution here
def transpose(matrix: list):
    for row in range(len(matrix)):
        for item in range(row):
           matrix[row][item], matrix[item][row] = matrix[item][row], matrix[row][item]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)

