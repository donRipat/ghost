from player import *

# with open("words_ge_4.txt", "r") as word_file:
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
    current_player = players[current_p_index]
    past_player = players[past_p_index]
    print(f"Current string: _{current_string}_")
    print(f"{current_player.name}'s move: ")
    inp = current_player.play(current_string, words)
    if current_player.__class__.__name__ != "HumanPlayer":
        print(inp)
    if inp == "":
        print(f"Make your move, {current_player.name}:")
        continue
    if inp[0] == ">":
        current_string += inp[1]
    elif inp[0] == "<":
        current_string = inp[1] + current_string
    elif inp[0] == "?":
        print(f'The word "{inp[1:]}" ' 
              f'{"exists" if inp[1:] in words else "doesn\'t exist"}')
        continue
    elif inp[0] == "!":
        print(f"{current_player.name} called a bluff")
        if any([current_string in word for word in words]):
            print(f"bluff call was INCORRECT\nPossible words are "
                  f"{[word for word in words if current_string in word][:20]}")
            winner = past_player
        else:
            print(f"bluff call was correct")
            winner = current_player
        break
    elif inp == ":":
        res = []
        for word in words:
            if current_string in word:
                res.append(word)
        print(f"Here's your hint, dweeb: {res[:10]}")
        continue
    if current_string in words and len(current_string) > 3:
        print(f"{current_player.name} spelled the word: {current_string}")
        winner = past_player
        break
    turn_counter += 1
print(f"{winner.name} WON!")
