from faker import Faker
fake = Faker()

class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def intriduce(self):
        return f"Hello, my name is {self.name} and my address is {self.address}"

student1 = Student(fake.name(), fake.address())
student2 = Student(fake.name(), fake.address())
student3 = Student(fake.name(), fake.address())
print(student1.intriduce())
print(student2.intriduce())
print(student3.intriduce())

"""Эта библиотека используется для создание фэйковых
 данных чтобы тестить или заполнят базу данных"""