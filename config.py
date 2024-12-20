with open("src/resources/words_ge_4.txt", "r") as word_file:
    WORDS = frozenset([str(word) for word in word_file.read().split()])
    print(f"{len(WORDS)} words loaded")