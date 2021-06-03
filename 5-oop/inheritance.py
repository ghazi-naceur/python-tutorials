class Animal():  # Base class
    def __init__(self):
        print("Animal created")

    def print_animal(self):
        print("This is an animal")

    def eat(self):
        print("Animal is eating")


class Dog(Animal):  # Derive class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def print_animal(self):
        print("This is a dog")

    def eat(self):
        print("Dog is eating")

    def bark(self):
        print("Dog is barking")


if __name__ == '__main__':
    animal = Animal()
    animal.print_animal()
    animal.eat()

    dog = Dog()
    dog.print_animal()
    dog.eat()