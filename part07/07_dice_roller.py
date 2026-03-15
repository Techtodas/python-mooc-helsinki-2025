# Write your solution here
from random import choice

def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
        }

    return choice(dices[die])

def play(die1: str, die2: str, times: int):
    p1_win = 0
    p2_win = 0
    tie = 0
    
    for i in range(times):
        p1 = roll(die1)
        p2 = roll(die2)

        if p1 > p2:
            p1_win += 1
        elif p2 > p1:
            p2_win += 1
        else:
            tie+=1

    return p1_win, p2_win, tie

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("C", "C", 1000)
    print(result)