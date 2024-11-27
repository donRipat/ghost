with open("words.txt", "r") as word_file:
    words = frozenset([str(word) for word in word_file.read().split()])
print(f"{len(words)} words loaded")
current_string = ""
while (True):
    print(f"_{current_string}_")
    inp = input()
    if inp[0] == ">":
        current_string += inp[1]
    elif inp[0] == "<":
        current_string = inp[1] + current_string
    elif inp[0] == "?":
        print(inp[1:] in words)
    if current_string in words and len(current_string) > 3:
        print(f"word spelled: {current_string}")
        break
