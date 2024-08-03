from character import Character, Item
from copy import copy, deepcopy

chacter_one = Character("Hero 1")
# character_copy = copy(chacter_one)
character_copy = deepcopy(chacter_one)

chacter_one.health -= 20
chacter_one.sword.name = "Sword 123456"
# chacter_one.sword = Item("Sword 123456")

# print(character_copy)
# print(chacter_one)
print(character_copy.sword)
print(chacter_one.sword)