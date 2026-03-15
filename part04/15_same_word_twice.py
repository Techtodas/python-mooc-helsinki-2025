# Write your solution here
word = []
i = 1
while True:
    user_word = input("Word: ")
    if user_word in word:
        print(f"You typed in {len(word)} different words")
        break
    word.append(user_word)