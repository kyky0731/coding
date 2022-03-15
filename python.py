class Dog:
  def __init__(self, name, type, is_ext, sci_name):
    self.name = name
    self.type = type
    self.is_ext = is_ext
    self.sci_name = sci_name
  def show_info_dog(self):
    return f'The name of the dog is {self.name}. The type of the dog is a {self.type}, and it is {self.is_ext} that it is extinct. The scientific name is {self.sci_name}.'
class Human:
  def __init__(self, name, age, race, gender):
    self.name = name
    self.age = age
    self.race = race
    self.gender = gender
  def show_info_human(self):
    return f"""The name of the human is {self.name}. The race of the human is {self.race}. The age of the human is {self.age}. The gender of the human is a {self.gender}."""

poodle = Dog('chloe', 'poodle', False, 'canus lupus familiaris')
kyle = Human('Kyle', 12, 'Asian: Taiwanese', 'boy')
print(Human.show_info_human(kyle))
print(Dog.show_info_dog(poodle))
