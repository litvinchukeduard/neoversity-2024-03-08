
class MyHuman:

    def __init__(self, name) -> None:
        self.name = name


class Human:
    name = 'Igor'

    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    language = ""

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    value = "Python"


class JSDeveloper(Developer):
    value = "JavaScript"


# p_dev = PythonDeveloper()
# p_dev.name = 'Bob'
# p_dev.voice()  # Hello! My name is Bob
# p_dev.make_some_code()  # My Programming language is Python

# js_dev = JSDeveloper()
# js_dev.make_some_code()  # My Programming language is JavaScript

human_one = Human()
human_two = Human()

Human.name = "Stepan"

# human_one.name = "Stepan"

# print(human_one.name)
# print(human_two.name)

# developer = PythonDeveloper()
developer = PythonDeveloper()

print(developer.make_some_code())

# print(dir(Human()))
# print()
# print(dir(developer))