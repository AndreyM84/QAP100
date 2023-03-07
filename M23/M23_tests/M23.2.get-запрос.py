"""Попробуем прочитать эти же тексты, но не через браузер,
а через наш Python-скрипт с помощью библиотеки Requests. Для этого отправим гет-запрос:"""

import requests

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)

# ответ: content

"""
 status_code, который говорит нам о том, какой вообще ответ пришёл. 
 Давайте поменяем наш код и посмотрим, что программа выведет теперь
"""
import requests

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.status_code)  # узнаем статус полученного ответа

# 200

"""
Давайте посмотрим на JSON-ответ, присланный нам с того же самого ресурса. Попробуем с помощью той же библиотеки Requests обращаться по адресу
https://baconipsum.com/api/?type=meat-and-filler"""

import requests

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
print(r.content)

"""чтобы использовать полученный ответ как Python-объект, надо воспользоваться дополнительной библиотекой, 
которая упрощает работу с JSON-ответами и может легко переконвертировать ответ от сервера в Python-объекты, 
с которыми удобно работать. Давайте поменяем наш код и превратим данный текст в список, на который он так сильно похож."""

import requests
import json  # импортируем необходимую библиотеку

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')

"""Теперь мы сделали ответ от сервера списком — структурой данных Python, с которой гораздо приятнее работать, чем просто с байтами.
Давайте посмотрим теперь на ещё один тип возвращаемых значений. Он тоже будет JSON, но в данном случае он, скорее, будет похож на словарь."""

import requests
import json

r = requests.get('https://api.github.com')

print(r.content)

"""Давайте всё же теперь сделаем его настоящим словарём."""

import requests
import json

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

# <class 'dict'>
# https://api.github.com/user/following{/target}

