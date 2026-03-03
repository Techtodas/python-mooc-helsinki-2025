# Write your solution here
from random import choice
def words(n: int, beginning: str):
    found_list = []
    rand_list = []

    with open("words.txt") as f:
        for l in f:
            l = l.strip()
            if l.startswith(beginning) and l not in found_list:
                found_list.append(l)

    if n > len(found_list):
        raise ValueError

    while len(rand_list) < n:
        rand_word = choice(found_list)
        if  rand_word not in rand_list:
            rand_list.append(rand_word)

    return rand_list
