# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.


# Пример простого декоратора
def my_decorator(func):  # 2

    def wrapper():
        print('Перед выполнением функции')  # 4
        func()  # 5
        print('После выполнением функции')  # 6

    return wrapper  # 3


@my_decorator
def hello():
    print("Привет мир!!")


# hello() # 1


# Декораторы с аргументами
# n = 3
def repeat(n):  # step 2
    # func = greet()
    def decorator(func):  # step 4
        def wrapper(*args, **kwargs):
            for i in range(n):  # step 6
                func(*args, **kwargs)  # step 6

        return wrapper  # step 5

    return decorator


@repeat(3)
def greet():
    print("Привет!!")


# greet() # step 1


# Декораторы для классов
# MyClass
def class_decorator(cls):
    # MyClass
    class NewClass(cls):

        def new_method(self):
            return print("Новый метод!!!")

    return NewClass


# class_decorator

@class_decorator
class MyClass:

    def old_method(self):
        return print("Старый метод")


# obj = MyClass() # NewClass()
# obj.old_method()
# obj.new_method()


class Person:

    # Конструктор | Магический метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self, ):
        return f"бла бла бла"


# obj = Person("Павел", 25)

# print(obj)


# 2. Магические методы
# Магические методы (или dunder-методы, от double underscore) — это методы, которые
# начинаются и заканчиваются двумя подчеркиваниями (__init__, __str__, __add__ и др.).
# Они позволяют переопределять стандартное поведение объектов.

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        print(f"{self.amount}------{other.amount}")
        return f'бла '

    def __str__(self, ):
        return f"{self.amount} som"

    def __len__(self):
        return f"pass"


m1 = Money(100)
m2 = Money(400)
# m2.__add__(other=m1)
m3 = m2 + m1
len(m3)


# 1. Декоратор @staticmethod
# Описание:
# Декоратор @staticmethod используется для того, чтобы определить метод, который не зависит от экземпляра класса
# (не использует self) и не зависит от самого класса (не использует cls). Такой метод можно вызывать без создания
# экземпляра класса.

class Math:

    @staticmethod
    def add(a, b):
        return a + b


# print(Math.add(1,2))


# 2. Декоратор @classmethod
# Описание:
# Декоратор @classmethod используется для определения метода, который принимает первым аргументом
# сам класс (не экземпляр). Этот аргумент обычно называется cls. Метод класса может изменять состояние класса,
#  но не работает с состоянием конкретного экземпляра.


class Person:
    count = 0
    password = "Def"

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_population(cls):
        return cls.count

    def test(self, ):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod  # Person
    def create_person(cls, name):
        return cls(name)
        # Person(John)


person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Bobs")
print(Person.get_population())
person4 = Person.create_person("jonh")
print(person4.name)

