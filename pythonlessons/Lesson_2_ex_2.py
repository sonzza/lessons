# Используя навыки работы с текстом, получите количество студентов GeekBrains со стартовой страницы сайта
# geekbrains.ru. Решите задачу двумя способами: a) используя регулярные выражения (библиотеку re), b) используя
# библиотеку BeautifulSoup. Примечание: Чтобы увидеть количество учеников, вам надо зайти на главную страницу сайта
# без залогинивания (нажмите 3 точки в правом верхнем углу экрана рядом с вашей фотографией и выберите пункт меню
# «Выход»). Вы окажетесь на главной странице, где вверху увидите логотип, количество человек (то, что нам нужно) и
# кнопку «Войти».

# используя регулярные выражения (библиотеку re)


import re
from bs4 import BeautifulSoup as bs

with open("geekbrains.html") as f:
    geek = f.read()


def re_func():
    total_users = re.compile(
        "<span class=\"total-users\">(Нас уже [\s0-9]+ человек)</span>")
    total_geeks = total_users.findall(geek)
    return total_geeks


print(re_func())

# используя библиотеку BeautifulSoup

geek_users = bs(geek, "html.parser")

# если нужно найти все варианты, удовлетворяющие задаче
total_u = geek_users.find_all(class_='total-users')
for n in total_u:
    print(n.contents)

# если нужен один (или первый) результат
total_user = geek_users.find(class_='total-users')
print(total_user.contents)
