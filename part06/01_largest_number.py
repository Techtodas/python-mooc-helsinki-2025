# write your solution here
import os 

def largest():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "numbers.txt")
    with open(filename) as new_file:
        largest_number = 0

        for number in new_file:
            converted_no = int(number)
            if converted_no > largest_number:
                largest_number = converted_no
    return largest_number
    
if __name__ == "__main__":
    print(largest())



