# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    result = []

    for p in range(amount):
        result.append(Fraction(1, amount))

    return result