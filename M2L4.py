"""простой декоратор"""
# def my_decorator(func):
#     def wrapper():
#         print('перед выполнений функций')
#         func()
#         print('опсле выполнений функций ')
#         return wrapper
#
# @my_decorator
# def hello():
#     print('привет мир')
# hello()
#
#
"""декотраторы с аргументами"""
# def repeat(n):
#     def  decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
# @repeat(3)
# def greet():
#     print("привет!!!!")
#
# greet()
#
# декоратор для классов
#
# def class_decorator(cls):
#     class NewClass(cls):
#         def new_method(self):
#             return print("новый метод")
#     return NewClass
# @class_decorator
# class MyClass:
#     def old_method(self):
#         return print("старый метод")
#
# obj = MyClass()
# obj.old_method()
# obj.new_method()
# конструктор или магический метод
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"blabla"
# obj = Person("Pavel",25 )
# print(obj)

# class Monkey:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __add__(self, other):
#         print(f"{self.amount}------{other.amount}")
#         return Monkey(self.amount + other.amount)
#
#     def __str__(self):
#         return f"{self.amount} som"
#
#     def __len__(self):
#         return f"pass"
#
# m1 = Monkey(100)
# m2 = Monkey(400)
# m3 = m1 + m2
# print(m3)

# class  Math:
#     @staticmethod
#     def add(self, a, b):
#         return a + b
# obj3 = Math()
#
# print(obj3.add(1, 2))
#

class Person:
    client = 123
    password = ""

    def __init__(self,name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_population(cls):
        return cls.count


    def test(self,):
        pass

    @classmethod
    def static_method(cls):
        pass



    @classmethod
    def create_person(cls,name):
        return cls(name)

person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Bobs")
print(Person.get_population())
person4 = Person