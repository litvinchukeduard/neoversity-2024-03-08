from character import DataCharacter

data_character_one = DataCharacter("Hero one")

print(data_character_one)
print([data_character_one])

# character_bad = None
try:
    character_bad = DataCharacter("")
except ValueError:
    print("Error happened")
# print(character_bad)