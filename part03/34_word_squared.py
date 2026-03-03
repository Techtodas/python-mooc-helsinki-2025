def squared(text, size):
    index = 0
    row_count = 0

    while row_count < size:
        row = ""
        char_count = 0

        while char_count < size:
            row = row + text[index]
            index = index + 1

            if index == len(text):
                index = 0

            char_count = char_count + 1

        print(row)
        row_count = row_count + 1


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
