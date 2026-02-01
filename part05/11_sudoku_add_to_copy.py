# Write your solutio
def print_sudoku(sudoku: list):
    for row in range(9):
        for square in range(9):
            if sudoku[row][square] == 0:
                print("_", end="")
                print(" ", end="")
            else:
                print(f"{sudoku[row][square]}", end="")
                print(" ", end="")
            if (square + 1) % 3 == 0:
                print(" ", end="")
        print()
        
        if (row + 1) % 3 == 0 and row != 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []

    for row in sudoku:
        new_list.append(row[:])

    new_list[row_no][column_no] = number
    
    return new_list
        
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)