"""
Створити клас, який буде представляти персонажи гри (name, health)
"""
from dataclasses import dataclass


class Item:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'Item({self.name})'

class Character:
    def __init__(self, name: str, health: int = 100) -> None:
        if len(name) == 0:
            raise ValueError
        self.name = name
        self.health = health
        self.inventory = []
        self.sword = Item("Sword")

    def add_item_to_inventory(self, item: Item):
        self.inventory.append(item)

    def __str__(self):
        return f"Character with name '{self.name}' and health: {self.health}"
    
    def __repr__(self) -> str:
        return f"Character({self.name}, {self.health})"

@dataclass
class DataCharacter:
    name: str
    health: int = 100

    def __post_init__(self):
        if len(self.name) == 0:
            raise ValueError





