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

    def __str__(self):
        """string method"""
        if self.has_horns:
            return f'{self.name} is a {self.height:.2f} m tall horned blork!'
        else:
            return f'{self.name} is a {self.height:.2f} m tall blork!'


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

    def __str__(self):
        """string"""
        return f'{self.model} ({self.year}), moving at {self.speed} km/h.'
