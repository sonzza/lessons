# Решить с помощью генераторов списка.
#
# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.

fruits = ['apple', 'pineapple', 'watermelon', 'kiwi', 'coconut', 'grape']
big_fruits = ['watermelon', 'pineapple', 'coconut', 'melon']

main_fruits = []

main_fruits = [fruit for fruit in fruits if fruit in big_fruits]

print(main_fruits)