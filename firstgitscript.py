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

  name = input('What is your name? ')
  age = input('What is the age of the human? If the species is not human, skip this step. ')
  race = input('What is the race of the human? If the species is not human, skip this step. ')
  gender = input('What is the gender of the human? If the species is not human, skip this step. ')
  is_ext = input('Is the dog extinct? If the species is not a dog, skip this step. ')
  
