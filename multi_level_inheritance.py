class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed
