from player import *

with open("words.txt", "r") as word_file:
    words = frozenset([str(word) for word in word_file.read().split()])
print(f"{len(words)} words loaded")
p1 = HumanPlayer("Rinat")
p2 = PrimitiveAI()
turn_counter = 0
current_string = ""
while (True):
    if turn_counter % 2 == 0:
        current_player = p1
    else:
        current_player = p2
    print(f"_{current_string}_")
    inp = current_player.play(current_string, words)
    if inp[0] == ">":
        current_string += inp[1]
    elif inp[0] == "<":
        current_string = inp[1] + current_string
    elif inp[0] == "?":
        print(inp[1:] in words)
    elif inp[0] == "!":
        if current_string in words:
            print("bluff call was INCORRECT")
            print(f"Player {current_player.name} lost :P")
        else:
            print("bluff call was correct")
            print(f"Player {current_player.name} won :)")
        break
    if current_string in words and len(current_string) > 3:
        print(f"word spelled: {current_string}")
        print(f"Player {current_player.name} lost :P")
        break
    turn_counter += 1
