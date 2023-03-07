"""
Сейчас мы попробуем создать класс LinkedList, реализующий список.
Элементы списка будут представлять собой экземпляры класса Node.
"""


# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
"""
На первом шаге добавим метод pushleft, который вставляет новый элемент в начало списка.
"""
    # def pushleft(self, value):
    #     if self.first is None:
    #         self.first = Node(value)
    #         self.last = self.first
    #     else:
    #         new_node = Node(value, self.first)
    #         self.first = new_node

"""
Задание 22.6.2
Напишите функцию pushright, которая добавляет элемент в правую часть списка.
"""
    # def pushright(self, value):
    #     if self.first is None:
    #         self.first = Node(value)
    #         self.last = self.first
    #     else:
    #         new_node = Node(value)
    #         self.last.next = new_node
    #         self.last = new_node
"""
создание двусвязного списка, в котором помимо указателя на следующий элемент будет храниться указатель и на предыдущий элемент. 
Или можно модифицировать односвязный список, сохраняя еще и указатель на предпоследний элемент.
"""
    # def popleft(self):
    #      if self.first is None: # если список пустой, возвращаем None
    #         return None
    #     elif self.first == self.last: # если список содержит только один элемент
    #         node = self.first # сохраняем его
    #         self.__init__() # очищаем
    #         return node # и возвращаем сохраненный элемент
    #     else:
    #         node = self.first # сохраняем первый элемент
    #         self.first = self.first.next # меняем указатель на первый элемент
    #     return node # возвращаем сохраненный

"""
И немного более сложная процедура удаления последнего элемента:
"""


# def popleft(self):
#     if self.first is None:
#         return None
#     elif self.first == self.last:
#         node = self.first  # сохраняем его
#         self.__init__()  # очищаем
#         return node  # и возвращаем сохраненный элемент
#     else:
#         node = self.first  # сохраняем первый элемент
#         self.first = self.first.next  # меняем указатель на первый элемент
#         return node  # возвращаем сохраненный


# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
# 
# print(LL)

"""Полный код в верном исполнении в M22.6.3"""