# Write your solution here
def histogram(char: str):
    groups = {}

    for letter in char:
        alphabet = letter[0]
        if alphabet not in groups:
            groups[alphabet] = []
        groups[alphabet].append(letter)

    for key, value in groups.items():
        print(key, "*"*len(value))
    
    return groups

if __name__ == "__main__":
    char = "statistically"

        