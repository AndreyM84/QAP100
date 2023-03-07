"""
Создадим файл rectangle_2.py в отдельной директории в папке (назовем её python_practice).
Выполним импорт класса Rectangle:
"""

from rectangle_2 import Rectangle

# создаем два прямоугольника:
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# вывод площади наших двух прямоугольников:
print(rect_1.get_area())
print(rect_2.get_area())

# Выполним импорт класса Square:
from rectangle_2 import Square

# создаем два квадрата:
square_1 = Square(5)
square_2 = Square(10)

# вывод площади наших двух квадратов:
print(square_1.get_area_square())
print(square_2.get_area_square())

# Создадим список экземпляров классов:
figures = [rect_1, rect_2, square_1, square_2]

# Далее пройдемся по циклу for:
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

"""
Это необходимо, чтобы найти площадь каждой фигуры, сохраненной в списке figures. Обратите внимание, мы будем работать с 
прямоугольниками и квадратами с помощью разных методов: get_area() и get_area_square(). 
Внутри цикла проверяем: 
- Если экземпляр класса figure является квадратом, то вызываем метод get_area_square().
- В противном случае — обрабатываем данные для прямоугольника методом get_area().
В условии есть функция isinstance, поддерживающая наследование. Она проверяет, является ли аргумент объекта экземпляром 
класса или экземпляром класса из кортежа. В случае если является, функция возвращает True, если не является — False. 
"""

from rectangle_2 import Circle
circle_1 = Circle(4)
circle_2 = Circle(12)

print(circle_1.get_area_circle(), circle_2.get_area_circle())

"""
Задание 21.8.2
Выполните задание, взяв за основу полученный код из задания 21.8.1. 
Добавьте еще один класс — круг (class Circle), который принимает в качестве аргументов свой радиус.
"""