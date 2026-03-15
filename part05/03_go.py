# Write your solution here
def who_won(game_board: list):
    p1_score = 0
    p2_score = 0

    for i in game_board:
        for square in i:
            if square == 1:
                p1_score+=1
            elif square == 2:
                p2_score+=1

    if p1_score > p2_score:
        return 1
    elif p2_score > p1_score:
        return 2
    else:
        return 0
            
if __name__ == "__main__":
    go = [[1]]
    print(who_won(go))