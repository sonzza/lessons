# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. Если
# список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.

import random

number_mas = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def random_func(numbers):
    if len(numbers) != 0:
        rand_numb = random.randint(0, len(numbers) - 1)
        number = numbers[rand_numb]
        return number
    else:
        return None


if __name__ == '__main__':
    print(random_func(number_mas))


