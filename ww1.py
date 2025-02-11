class Hero:
    def init(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def introduce(self,):
        print(f'Привет меня зовут {self.name}, мой лвл:{self.lvl}, мое здоровье:{self.hp}')
    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False
doni = Hero("ДОНИ", 25, 100)
doni.introduce()
adil = Hero("Адиль", 9, 100)
aza = Hero("Аза", 32, 100)
print(adil.is_adult())
print(aza.is_adult())