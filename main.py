from player import *

with open("words_ge_4.txt", "r") as word_file:
    words = frozenset([str(word) for word in word_file.read().split()])
print(f"{len(words)} words loaded")
p1 = HumanPlayer("Rinat")
p2 = PrimitiveAI()
move_order = input(f"Who moves first?\n(0) {p1.name} (1) {p2.name}: ")
if (move_order == "1"):
    players = [p2, p1]
else:
    players = [p1, p2]
turn_counter = 0
current_string = ""
while (True):
    current_p_index = turn_counter % 2
    past_p_index = (turn_counter + 1) % 2
    print(f"Current string: _{current_string}_")
    inp = players[current_p_index].play(current_string, words)
    if inp[0] == ">":
        current_string += inp[1]
    elif inp[0] == "<":
        current_string = inp[1] + current_string
    elif inp[0] == "?":
        print(inp[1:] in words)
        continue
    elif inp[0] == "!":
        print(f"{players[current_p_index].name} called a bluff")
        if any([current_string in word for word in words]):
            print(f"bluff call was INCORRECT")
            print([word for word in words if current_string in word][:20])
            winner = players[past_p_index]
            #print(f"Player {players[current_p_index].name} lost :P")
        else:
            print(f"bluff call was correct")
            winner = players[current_p_index]
            #print(f"Player {players[current_p_index].name} won :)")
        break
    if current_string in words and len(current_string) > 3:
        print(f"{players[current_p_index].name} spelled the word: {current_string}")
        winner = players[past_p_index]
        #print(f"Player {players[current_p_index].name} lost :P")
        break
    turn_counter += 1
print(f"{winner.name} WON!")
