# Write your solution here
import string
from random import choice

def generate_password(length: int):
    final_pass = ""
    
    for i in range(length):
        final_pass += choice(string.ascii_lowercase)
    return final_pass

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))