import random
class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        self.hp += 1000
        return f"Hp Plus 1000"

    def attack(self):
        return f"{self.name} attacks someone"


class Arther(Heroes):
    def __init__(self, name, hp, arrows, precision ):
        super().__init__(name,hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows <1:
            return "у вас нет стрел"
        self.arrows -= 1
        if random.randint(1, 100) < self.precision:
            return f"{self.name} попал в цель"
        else:
            return f"{self.name} не попал"

    def rest(self):
        self.arrows += 5
        return f"количество стрел увеличелось до {self.arrows}"

    def status(self):
        return f"Имя {self.name}\n Здоровье: {self.hp}\n Количество стрел: {self.arrows}\n Точность: {self.precision} "


arther1 = Arther("doni", 100, 24, 99)
print(arther1.attack())
print(arther1.rest())
print(arther1.status())















