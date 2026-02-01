# Write your solution here
def play_turn(game_board: list, x: int, y, piece: str):

    if y >= len(game_board) or y < 0 or x >= len(game_board[y]) or x < 0:
        return False
    elif game_board[y][x] != '':
        return False
    else:
        game_board[y][x] = piece
        return True


if __name__ == "__main__":
    game_board = [["x", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 0, 0, "X"))
    print(game_board)