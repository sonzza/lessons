# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы,
# например: my_favourite_group = { 'name': 'Г.М.О.', 'tracks': ['Последний месяц осени', 'Шапито'], 'Albums': [{
# 'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]} С помощью модулей json и pickle
# сериализовать данный словарь в json и в байты, вывести результаты в терминал. Записать результаты в файлы
# group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8. 2: Создать модуль
# music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. И
# получить объект: словарь из предыдущего задания.
import pickle
import json

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]
}

with open('group.pickle', 'wb') as boo:
    pickle.dump(my_favourite_group, boo)

with open('group.pickle', 'r') as boo:
    boo_pickle = pickle.dumps(my_favourite_group)
    print(f'{boo_pickle}')

with open('group.pickle', 'rb') as boo:
    print(pickle.load(boo))

with open('group.json', 'w', encoding='utf-8') as bo:
    json.dump(my_favourite_group, bo)

with open('group.json', 'r') as boo:
    bo_json = json.dumps(my_favourite_group)
    print(f'{bo_json}')

with open('group.json', 'r') as bo:
    print(json.load(bo))
