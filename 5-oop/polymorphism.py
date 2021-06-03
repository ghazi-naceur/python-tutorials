class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + " the dog is barking"


class Cat(Animal):
    def speak(self):
        return self.name + " the cat is meowing"


def pet_speak(pet):
    print(pet.speak())


if __name__ == '__main__':
    rex = Dog("Rex")
    print(rex.speak())

    meawouth = Cat("Meawouth")
    print(meawouth.speak())

    for pet in [rex, meawouth]:
        print(type(pet))
        print(pet.speak())

    pet_speak(rex)
    pet_speak(meawouth)
