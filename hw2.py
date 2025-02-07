class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} готовится к битве!")

    def attack(self):
        print(f"{self.name} наносит удар!")

class Archen(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision > 1:
                print(f"{self.name} успешно попал ! Осталось стрел :{self.arrows}")
            else:
                print(f"{self.name} промахнулся. Осталось стрел :{self.arrows}")
        else:
            print(f"{self.name} не может атаковать, не осталось стрел")
    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил запс стрел! Тепрь их :{self.arrows}")

    def status(self):
        return (f"Герой {self.name}, здоровье {self.hp}, стрелы {self.arrows},"
                f" точность {self.precision}")
archer = Archen("Макото",100,1,1.1)
archer.action()
archer.attack()
archer.rest()
print(archer.status())