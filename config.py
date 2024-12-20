with open("src/resources/words_ge_4.txt", "r") as word_file:
    WORDS = frozenset([str(word) for word in word_file.read().split()])
    print(f"{len(WORDS)} words loaded")

with open("src/resources/top_first_letters", "r") as file:
    Top_First_Letters = file.read().split()

with open("src/resources/top_last_letters", "r") as file:
    Top_Last_Letters = file.read().split()
