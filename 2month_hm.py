class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduse(self):
        print(f"привет ,меня зовут <{self.name}> мои lvl <{self.lvl}>  мое hp <{self.hp}>")

    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False

piter = Hero('spider man',11,20)

piter.introduse()

super_man = Hero('super man',10,240)
bat_man = Hero('batman',9,140)

print(super_man.is_adult())
print(bat_man.is_adult())