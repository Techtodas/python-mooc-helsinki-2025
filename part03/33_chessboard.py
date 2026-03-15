# Write your solution here
def chessboard(rows):
    counter = 1
    while counter <= rows:
        char1 = "10"*rows
        char2 = "01"*rows
    
        print(char1[:rows])

        if counter+1 <= rows:
            print(char2[:rows])

        counter+=2

# Testing the function
if __name__ == "__main__":
    chessboard(3)
