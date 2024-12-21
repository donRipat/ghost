import yaml

with open('config.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

with open(CONFIG["resources"]["words_ge_4"], "r") as word_file:
    WORDS = frozenset([str(word) for word in word_file.read().split()])
    print(f"{len(WORDS)} words loaded")

with open(CONFIG["resources"]["top_first_letters"], "r") as file:
    Top_First_Letters: dict[str, float] = {}
    for line in file:
        key, value = line.split(":", 1)
        Top_First_Letters[key] = float(value)

with open(CONFIG["resources"]["top_last_letters"], "r") as file:
    Top_Last_Letters: dict[str, float] = {}
    for line in file:
        key, value = line.split(":", 1)
        Top_Last_Letters[key] = float(value)
