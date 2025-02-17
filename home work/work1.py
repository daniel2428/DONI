class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return (f'Привет меня зовут {self.name}, мой лвл:{self.lvl}, мое здоровье:{self.hp}')

superman =Hero("Klarkent" , 15, 200)
