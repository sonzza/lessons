# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def max_func():
    numbers = []
    for i in range(3):
        number = int(input("Введите число: "))
        numbers.append(number)
    return max(numbers)


print('Максимальное число', max_func())
