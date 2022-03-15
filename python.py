class Dog:
  def __init__(self, name, type, is_ext, sci_name):
    self.name = name
    self.type = type
    self.is_ext = is_ext
    self.sci_name = sci_name
  def show_info(self):
    return f'The name of the dog is {self.name}. The type of the dog is a {self.type}, and it is {self.is_ext} that it is extinct. The scientific name is {self.sci_name}.'


poodle = Dog('chloe', 'poodle', False, 'canus lupus familiaris')

print(Dog.show_info(poodle))
