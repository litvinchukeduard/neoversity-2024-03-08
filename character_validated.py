'''Додати валідацію до поля name, щоб воно не було пустим'''

class Character:
    def __init__(self, name: str, health: int = 100) -> None:
        self.__name = None
        self.name = name
        self.health = health
        self.inventory = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name: str):
        if len(new_name) == 0:
            raise ValueError("Name should not be empty")
        self.__name = new_name

    def __str__(self):
        return f"Character with name '{self.name}' and health: {self.health}"
    
    def __repr__(self) -> str:
        return f"Character({self.name}, {self.health})"
    

# character = Character("Hero")
# # print(character.__name)
# print(dir(character))
# # print(character._Character__name)
# # character._Character__name = "Hero1"
# # print(character._Character__name)
# # character._name = "" # BAD!

# print(character.name) # Getter
# character.name = "Hero 1" # Setter
# print(character.name)

# character.name = ""
Character("")