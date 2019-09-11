my_list_1 = [2, 5, 8, 2, 12, 12, 4, 5, 55, 77, 8, 8, 3, 7]
my_list_2 = [2, 7, 12, 3, 77, 8, 56]

# Если имелось ввиду удалить относительно количества таких же элементов во втором списке

for my_objective in my_list_2:
    if my_objective in my_list_1:
        my_list_1.remove(my_objective)
print(my_list_1)

# Если нужно удалить все совпадающие элементы

my_list_1 = [2, 5, 8, 2, 12, 12, 4, 5, 55, 77, 8, 8, 3, 7]
my_list_2 = [2, 7, 12, 3, 77, 8, 56]

for my_objective in my_list_2:
        while my_objective in my_list_1:
            my_list_1.remove(my_objective)
print(my_list_1)
