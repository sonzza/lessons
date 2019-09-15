# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. Вызовите
# каждую функцию в main.py и проверьте что все работает как надо.


import Lesson_5_part_1
from Lesson_5_part_2 import random_func

Lesson_5_part_1.add_dir()
Lesson_5_part_1.del_dir()

test_mas = [5, 15, 10, 25, 12, 45]

print(random_func(test_mas))
