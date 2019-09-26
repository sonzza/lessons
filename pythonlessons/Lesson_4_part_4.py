# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони
# персонажа) Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле
# damage / armor Следовательно, у вас должно быть 2 функции: Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья
# персонажа.


player = {'name': None, 'armor': 1.2, 'health': 100, 'damage': 50}
enemy = {'name': None, 'armor': 1.2, 'health': 100, 'damage': 50}

player['name'] = input('Введите имя игрока: ')
enemy['name'] = input('Введите имя противника: ')


def attack(person_1, person_2):
    def person_damage():
        return int(person_1['damage']/person_2['armor'])
    person_2['health'] = person_2['health'] - person_damage()
    return person_2['health']


while player['health'] > 0 or enemy['health'] > 0:
    attack(player, enemy)
    attack(enemy, player)
    print(player)
    print(enemy)

