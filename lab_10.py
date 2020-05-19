"""
self is a parameter that references the object itself.
From within a (normal) method of a class, you can access an object's data attributes using self.
The first parameter of any (normal) method of a class is (or should be) self.
class Automobile:
Automobile()
my_car.go()
An object is an instance of a class.
In software, an object is an entity that can have both attributes and methods.
Creating a new class creates a new type.
'This is the text' is an argument passed to the constructor of the str class.
my_str.startswith('T') invokes (i.e. calls) the startswith() method on the my_str object.
my_str is an instance of the str type.
"""


"""File for creating Person objects"""


class Person:
    """Defines a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: bmi()
    """

    def __init__(self, name, age, weight, height):
        """Creates a new Person object with the specified name, age, weight
           and height"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        """Returns the body mass index of the person"""
        return self.weight / (self.height * self.height)

    def status(self):
        """returns status"""
        if self.bmi() < 18.5:
            return  'Underweight'
        elif 18.5 <= self.bmi() < 25:
            return 'Normal'
        elif 25 <= self.bmi() < 30:
            return 'Overweight'
        else:
            return 'Obese'


class Blork:
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool
    """

    def __init__(self, name, height, has_horns=False):
        """Creates a new Blork object"""
        self.name = name
        self.height = height
        self.has_horns = has_horns

    def say_hello(self):
        """says hello"""
        phrase = f'Hi! My name is {self.name.capitalize()}!'
        if not self.has_horns:
            print(phrase)
        else:
            print(phrase.upper())


class Car:
    """car class"""
    def __init__(self, model, year, speed=0):
        """initialises"""
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """accelerates"""
        self.speed += 5

    def brake(self):
        """brakes"""
        self.speed -= 5
        self.speed = max(0, self.speed)

    def honk_horn(self):
        """honks"""
        print(f"{self.model} goes 'beep beep'")
