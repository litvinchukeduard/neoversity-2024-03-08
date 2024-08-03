from abc import ABC, abstractmethod

class Developer(ABC):
    """
    Abstract class for a developer
    """
    field_description = "My Programming language"
    language = ""

    @abstractmethod
    def make_some_code(self):
        pass
        
    

class PythonDeveloper(Developer):
    value = "Python"

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class JSDeveloper(Developer):
    value = "JavaScript"

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"

developer = PythonDeveloper()
print(developer.make_some_code())