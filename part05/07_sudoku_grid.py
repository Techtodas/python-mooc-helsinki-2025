# Write your solution here
def row_correct(sudoku: list, row_no: int):
    memory = []

    for item in sudoku[row_no]:
        if item > 0 and item in memory:
            return False
        memory.append(item)

    return True


def column_correct(sudoku: list, column_no: int):
    memory = []

    for column in sudoku:
        if column[column_no] > 0 and column[column_no] in memory:
            return False
        memory.append(column[column_no])

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    seen_number = []

    for row in range(row_no, row_no + 3):
      for column in range(column_no, column_no + 3):
        if sudoku[row][column] > 0 and sudoku[row][column] in seen_number:
          return False

        seen_number.append(sudoku[row][column])

    return True


def sudoku_grid_correct(sudoku: list):

    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False

    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False

    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            if not block_correct(sudoku, start_row, start_col):
                return False

    return True

if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))