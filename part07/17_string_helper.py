# Write your solution here
import string

def change_case(orig_string: str):
    new_version = ""
    for i in orig_string:
        if i.islower():
            new_version += i.upper()
        else:
            new_version += i.lower()

    return new_version


def split_in_half(orig_string: str):
    mid = 0
    if len(orig_string.strip()) % 2 == 1:
        mid = len(orig_string) // 2
    else:
        mid = len(orig_string) // 2
    
    return orig_string[:mid], orig_string[mid:]


def remove_special_characters(orig_string: str):
    clean = ""
    for ch in orig_string:
        if ch in string.ascii_letters or ch in string.digits or ch == " ":
            clean += ch

    return clean

