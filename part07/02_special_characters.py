# Write your solution here
import string
def separate_characters(my_string: str):
    low_upp_letters = ""
    punc_char = ""
    char_left = ""

    for ch in my_string:
        if ch in string.ascii_letters:
            low_upp_letters += ch
        elif ch in string.punctuation:
            punc_char += ch
        else:
            char_left += ch

    return (low_upp_letters, punc_char, char_left)
