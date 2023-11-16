# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"


# Animal Parent Class

class Animal:
    def __init__(self, number_legs, primary_color):
        self.legs = number_legs
        self.color = primary_color

    def describe(self):
        string = self.__class__.__name__
        string += " has "
        string += str(self.legs) + " legs and is primarily "
        string += self.color
        return string

a = Animal(4, "green")
print(a.describe())

class Dog(Animal):
    def __init__(self, color):
        super().__init__(4, color)

    def speak(self):
        return "Bark"

class Cat(Animal):
    def __init__(self, color):
        super().__init__(4, color)

    def speak(self):
        return "Miao"

class Snake(Animal):
    def __init__(self, color):
        super().__init__(0, color)

    def speak(self):
        return "Ssssssss!"

fido = Dog("brown")
print(fido.speak())

mittens = Cat("orange")
print(mittens.speak())

slyther = Snake("green")
print(slyther.speak())
