from faker import Faker

fake = Faker()


class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def introduse(self):
        return f"Hi my name is {self.name} my address: {self.address}"

student1 = Student(fake.name(), fake.address())
print(student1.introduse())


# Устанавливаем библиотеку Faker: pip install faker
# Faker — это библиотека для генерации фейковых данных (имен, адресов, телефонов и т. д.).
# Она полезна для тестирования и разработки, когда нужны случайные данные.