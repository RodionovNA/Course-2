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
    """
    Abstract class with abstract method, all animals have sound
    """
    @abstractmethod
    def sound(self):
        """
        What sound makes animal
        """
        pass
    def do_you_real(self):
        """Give the answewr to question "do you real?"

        Returns:
            str: yes
        """
        return "Yes"


class Monkey(Animal):
    """
    Models a human of the past
    """
    POPULATION_MONKEY = 0

    def sound(self):
        """
        Give what sound makes the animal
        Returns:
            String: animal sound
        """
        return "O-a-o-a..."
    def how_much_polulation(self):
        """Give the population of monkey

        Returns:
            int: count of monkey
        """
        return self.POPULATION_MONKEY
    def what_eat(self):
        """
        Give favorite eat
        Returns:
            str: favorite eat
        """
        return self.must_have_eat
    def __init__(self, height, weight, eat = "banana"):
        if height <= 0 or weight <= 0:
            raise AttributeError("Height and weight must be more then zero.")
        Monkey.POPULATION_MONKEY += 1
        self.height = height
        self.weight = weight
        self.must_have_eat = eat


class Human(Monkey):
    """
    Model a human today

    Attributes:
        height: float
        width: float
        gender: str
    Class atributes:
        POPULATION_HUMAN: int
    """
    POPULATION_HUMAN = 0

    def __init__(self, height, width, gender, is_smart):
        super().__init__(height, width)
        self.gender = gender
        self.is_smart = is_smart
        Human.POPULATION_HUMAN += 1

    def icq(self):
        """
        Give the ICQ

        Returns:
            int: result of icq
        """
        if self.gender == "male": # ?
            return 120
        if self.gender == "female":
            return 50
        return 0
    def do_you_smart(self):
        """Give the answer "is he smart?"

        Returns:
            bool: yes - is smart, no - is not smart
        """
        return self.is_smart


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
        """Add thing to list

        Args:
            thing_name (str): name of thing
        """
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
