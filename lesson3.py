# Наследование - Инкапсуляция - полимарфизм - абстракция
from abc import abstractmethod



class Animel(ABC):




    @abstractmethod


    def make_sound(self):
     pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animel):
    def make_sound(self):
        return print(Gaf,gaf)



