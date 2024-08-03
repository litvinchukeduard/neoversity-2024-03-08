from character import Character, Item
from json_serialization import serialize_to_json, deserialize_character_from_json

character_one = Character("Hero")
print(character_one)

# charter_list = [Character("Hero 2"), Character("Hero 3")]
# print(charter_list)

sword = Item("Sword 1")
character_one.add_item_to_inventory(sword)


# print(dir(character_one))
character_one.power = 120
print(character_one.__dict__)

serialize_to_json(character_one, 'character.json')
deserialized_character = deserialize_character_from_json('character.json')

for item in deserialized_character.inventory:
    print(item)

# character_bad = Character("")
character_one.name = ""
