# Write your solution here
def read_input(prompt: str, start: int, end: int):
    while True:
        try:
            ask_user = int(input(prompt))
            if ask_user in range(start, end + 1):
                return ask_user
        except ValueError:
            pass

        print(f"You must type in an integer between {start} and {end}")
