# Write your solution here
def all_the_longest(my_list):
    longest_len = 0
    longest_word = []
    
    for i in my_list:
        if len(i) > longest_len:
            longest_len = len(i)
            longest_word = [i]
        elif len(i) == longest_len:
            longest_word.append(i)

    return longest_word

if __name__ == "__main__":
    my_list = ["aaaa", "bb", "cccccc"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']