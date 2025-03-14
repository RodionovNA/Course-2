"""
Необходимо будет реализовать последовательную 
иерархию из 3 классов (абстрактные классы не 
учитываются), 
учитывая все рассказанное на 1 паре и завтра. 
Каждый не менее 3 собственных атрибутов и 5 
собственных методов)
Выбор тематики зависит лишь от полета Вашей 
фантазии. Соблюдение code-style, разумеется, 
обязательно 
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Monkey(Animal):
    """
    Models a human of the past
    """
    POPULATION_MONKEY = 0

    def sound(self):
        return "O-a-o-a..."
    
    def __init__(self, height, weight):
        if height <= 0 or weight <= 0:
            raise AttributeError("Height and weight must be more then zero.")
        Monkey.POPULATION_MONKEY += 1
        self.height = height
        self.weight = weight


class Human(Monkey):
    """
    Models a human today
    """
    POPULATION_HUMAN = 0

    def __init__(self, height, width, gender):
        super().__init__(height, width)
        self.gender = gender
        Human.POPULATION_HUMAN += 1
        
    def ICQ(self):
        if self.gender == "male":
            return 135
        elif self.gender == "female":
            return 50
        else:
            return 0
        

class EvolutionalHuman(Human):
    """
    Models a human of the future
    """
    POPULATION_EHUMAN = 0
    things = list()

    def __init__(self, height, width, gender, density, regeneration):
        super().__init__(height, width, gender)
        self.density = density
        self.regeneration = regeneration
        EvolutionalHuman.POPULATION_EHUMAN += 1

    def create_thing(self, thing_name):
        EvolutionalHuman.things.append(thing_name)



try:
    me = Human(178, 64, "male")
    future_me = EvolutionalHuman(178, 64, "male", 0.314, 10)

except Exception:
    print("Could not create a class copy...")

else:
    print(me.sound())
    print(me.POPULATION_HUMAN)
    future_me.create_thing("table")
