import json
from character import Character, Item

def serialize_to_json(obj, file_path):
    with open(file_path, 'w') as file:
        json.dump(obj, file, default=lambda o: o.__dict__)

def deserialize_character_from_json(file_path) -> Character:
    with open(file_path, 'r') as file:
        data = json.load(file)
        new_character = Character(data['name'], data['health'])
        # new_character.inventory = 
        for item in data['inventory']:
            new_character.inventory.append(Item(item['name']))

        return new_character

