# Nikita.kg
# Twilio.com

# Наследование - Инкапсуляция - Полиморфизм - Абстракция
from abc import ABC, abstractmethod

import random


class OTPSrvice(ABC):

    @abstractmethod
    def sms_send():
        pass


class NikitaOTP(OTPSrvice):

    def sms_send(self, phone):
        phone = input("Вввудите тел в формате +996ххх хх хх хх")


class TwilioOTP(OTPSrvice):

    def sms_send(self, phone):
        phone = input("Вввудите тел в формате +7ххх хх хх хх хх")


class Animel(ABC):

    # Декоратор @abstractmethod
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animel):

    def make_sound(self):
        return print('Gaf gaf')

    def move(self):
        return print('run')


# dog = Dog()
# dog.make_sound()


from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

