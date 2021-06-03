class Hunter():

    # class object instance
    # same for any instance of a class
    nen_users = "Enhancer"

    def __init__(self, name, age, adult):
        self.name = name
        self.age = age
        self.adult = adult

    def print(self):
        print(f"He is {self.name}, {self.age}, {self.adult}")


class Circle():

    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
         self.radius = radius
         self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


if __name__ == '__main__':
    person = Hunter(name="Isaac", age=125, adult=True)
    print(person.name)
    print(person.age)
    print(person.adult)
    print(person.nen_users)

    person.print()

    circle = Circle(radius=30)
    print(circle.pi)
    print(circle.area)
    print(circle.get_circumference())

