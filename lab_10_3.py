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
        self.baranges = 0

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

    def collect_baranges(self, number=1):
        """collects balanges"""
        self.baranges += number

    def eat(self):
        """eats baranges"""
        if self.baranges >= 1:
            self.baranges -= 1
            self.height += 0.1
        else:
            print("I don't have any baranges to eat!")

    def feast(self):
        """feasts on baranges"""
        if self.baranges >= 5:
            if not self.has_horns:
                self.has_horns = True
            else:
                self.height *= 1.5
            self.baranges -= 5
        else:
            print("I don't have enough baranges to feast!")


class Whosit:
    def __init__(self, level, name, health):
        """inits"""
        self.level = level
        self.name = name
        self.health = max(health, 0)

    def __str__(self):
        """str"""
        return f'{self.name} ({self.level}), health = {self.health:.1f}'

    def suffer(self):