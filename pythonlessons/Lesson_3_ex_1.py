# 1. Напишите функцию получения IATA-кода города из его названия, используя API Aviasales для усовершенствования
# приложения по парсингу информации об авиабилетах, созданного нами в ходе урока. Примечание: воспользуйтесь
# документацией по API, которая доступна на странице www.aviasales.ru/API (ссылка на значке «API-документация»). Вам
# необходимо изучить раздел «API для определения IATA-кода».

import requests

origin_name = input("Введите название города, из которого планируете вылететь: ")
destination_name = input(("Введите название города, в который планируете прилететь: "))


def load_iatas(orig, dest):
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{}%20в%20{}".format(orig, dest)
    iatas = requests.get(link).json()
    origin = iatas["origin"]["iata"]
    destination = iatas["destination"]["iata"]
    return origin, destination


try:
    city_list = load_iatas(origin_name, destination_name)
    print(city_list)
    link_cal = requests.get("http://min-prices.aviasales.ru/calendar_preload?origin={}&destination={}".format(city_list[0], city_list[1]))
except KeyError:
    print('Город не найден')
else:
    print(link_cal.text)
    print(link_cal.json()['best_prices'][0]['value'])
