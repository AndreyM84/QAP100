"""
Импортируем класс Cat из файла cat_class:
"""
from cat_class_2 import Cat

cats = [
    {
        "species": "кошка",
        "name": "Барсик",
        "gender": "мальчик",
        "age": 3,
    },
    {
        "species": "кошка",
        "name": "Мурка",
        "gender": "девочка",
        "age": 5,
    }
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)

    print(f"\nВид: {cat_obj.species}\nИмя: {cat_obj.name}\nПол: {cat_obj.gender}\nВозраст: {cat_obj.age}\n")
