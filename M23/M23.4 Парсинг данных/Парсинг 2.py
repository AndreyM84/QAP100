"""теперь попробуем собрать заголовки всех новостей с Python.org.
Но для этого сейчас мы рассмотрим немного другой подход парсинга.
Сохраним HTML-страничку и поместим её в папку со скриптом, т. к. метод, который мы рассмотрим дальше,
будет работать с HTML-файлом."""

import requests
import lxml.html
from lxml import etree
html = requests.get('https://www.python.org/').content
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
ul = tree.findall('/body/div/section/div[2]/div[1]/div/ul/li[2]')
for li in ul:
    a = li.find('a')
    print(a.text)

# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html',
#                    lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.
#
# ul = tree.findall(
#     'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
#
# # создаём цикл? в котором будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find(
#         'a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
#     print(a.text)  # из этого тега забираем текст — это и будет нашим названием