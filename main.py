# Class Intro

# Our base class; no parens needed in definition
class Animal:
  def __init__(self, species, leg_num=0, domesticated=False):
    self.species = species
    self.leg_num = leg_num
    self.domesticated = domesticated

  def saySomething(self):
    if self.species == "dog":
      return "Woof"
    else:
      return "moosqueekrrrrchirp"

  def __str__(self):
    return f"This Animal is a {self.species} with {self.leg_num} legs that says {self.saySomething()}"

if __name__ == "__main__":
  dog = Animal("dog", 4, True)
  print(dog)



class Dog(Animal):
  def __init__(self, breed):
    self.breed = breed
    super().__init__("dog", leg_num=4, domesticated=True)

  def speak(self):
    return f"I am a dog, so I say {self.saySomething()}"



class Pet:
  def __init__(self, name, critter_instance):
    self.name = name
    self.animal_type = critter_instance

  def set_owner(self, name, phone):
    self.owner_name = name
    self.owner_number = phone

  def __str__(self):
    return f"This pet's name is {self.name}. It has {self.animal_type.leg_num} legs and it likes to say {self.animal_type.saySomething()}!"

aussie_mix = Dog("Aussie/Border Collie Mix")
murph = Pet("Murphis", aussie_mix)
murph.set_owner("The Sheps", "555-555-1234")

print(murph)