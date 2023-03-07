"""
Импортируем класс Cat из файла cat_class:
"""
from cat_class import Cat

# Создаем объект cat1:
cat1 = Cat("Барон", "мальчик", 2)
print(f"\nВид: {cat1.species}\nИмя: {cat1.name}\nПол: {cat1.gender}\nВозраст: {cat1.age}\n")

# Создаем объект cat2:
cat2 = Cat("Сэм", "мальчик", 2)
print(f"\nВид: {cat2.species}\nИмя: {cat2.name}\nПол: {cat2.gender}\nВозраст: {cat2.age}\n")
