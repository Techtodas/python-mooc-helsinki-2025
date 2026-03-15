# Write your solution here
import string as s
from random import choice, shuffle

def generate_strong_password(length: int, number=False, special_char=False):
    gen_pass = []
    allowed = s.ascii_lowercase

    if number:
        gen_pass.append(choice(s.digits))
        allowed += s.digits
    if special_char:
        gen_pass.append(choice("!?=+-()#"))
        allowed += "!?=+-()#"

    gen_pass.append(choice(s.ascii_lowercase))
            
    while len(gen_pass) < length:
        gen_pass.append(choice(allowed))

    shuffle(gen_pass)        
    return "".join(gen_pass)