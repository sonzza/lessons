# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


def your_data(name, age, city):
    return '{}, {} год(а)/лет, проживает в городе {}'.format(name, age, city)


print(your_data(input('Введите имя: '), input('Введите возраст: '), input('Введите город: ')))
