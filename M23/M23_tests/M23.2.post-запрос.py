import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет


"""
Давайте посмотрим, как с помощью уже знакомой нам библиотеки отправить данные в нужном нам формате:"""

import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)

"""Задание 23.2.3
Напишите программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис). 
Выведите первый из сгенерированных текстов."""

import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')

r = json.loads(r.content)

print(r[0])

