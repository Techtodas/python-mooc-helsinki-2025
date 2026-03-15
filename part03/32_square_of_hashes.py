# Write your solution here
# You can test your function by calling it within the following block
def hash_square(length):
    counter = length
    while counter > 0:
        print("#"*length)
        counter-=1

if __name__ == "__main__":
    hash_square(5)