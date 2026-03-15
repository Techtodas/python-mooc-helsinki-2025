# Write your solution here
def find_words(search_term: str):
    matches = []
    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            len_term = len(search_term)
            match = True
            if search_term.startswith("*"):
                if word.endswith(search_term[1:]):
                    matches.append(word)
            elif search_term.endswith("*"):
                if word.startswith(search_term[:-1]):
                    matches.append(word)

            if len(word) != len_term:
                continue
            for i in range(len(word)):
                if search_term[i] == ".":
                    continue
                elif word[i] != search_term[i]:
                    match = False

            if match:
                matches.append(word)

    return matches
#print(find_words("ca*"))