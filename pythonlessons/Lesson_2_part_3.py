my_list_1 = [2, 2, 5, 12, 8, 2, 12, 2, 5, 8, 2, 12, 12, 4, 5, 55, 77, 8, 8, 3, 7]

for my_objective in my_list_1:
    while my_objective in my_list_1:
        my_list_1.remove(my_objective)

print("Без повторений - ", my_list_1)

