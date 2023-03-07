"""
Создадим конструктор класса Cat со следующими параметрами: имя, пол, возраст:
"""
class Cat:

    species = "кошка"

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age