# Write your solution here
def most_common_character(character: str):
    counter = 0
    high_char = ""

    for i in character:
        if character.count(i) > counter:
            counter = character.count(i)
            high_char = i
    return high_char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))