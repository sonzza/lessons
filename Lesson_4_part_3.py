# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.


player = {'name': None, 'health': 100, 'damage': 50}
enemy = {'name': None, 'health': 100, 'damage': 50}

player['name'] = input('Введите имя игрока: ')
enemy['name'] = input('Введите имя противника: ')


def attack(person_1, person_2):
    person_2['health'] = person_2['health'] - person_1['damage']
    return person_2['health']


while player['health'] > 0 or enemy['health'] > 0:
    attack(player, enemy)
    attack(enemy, player)
    print(player)
    print(enemy)
