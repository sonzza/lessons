# 1. Получите текст из файла. Примечание Можете взять свой текст или воспользоваться готовым из материалов к уроку.
# Вспомните операции с чтением файлов и не забудьте сохранить текст в переменную по аналогии с видеоуроками.
import re

hw_list = ''
with open('home_work_1_1.txt', 'r', encoding='utf-8') as f:
    hw_list = f.read()
# print(hw_list)

# 2. Разбейте полученные текст на предложения.
# Примечание: Напоминаем, что в русском языке предложения заканчиваются на ., ! или ?.

sep = '\.\s|\?|\!'
print(re.split(sep, hw_list))

# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
# Пример вывода: [(“привет”, 3), (“люди”, 3), (“город”, 2)].


four_and_more_letters = '[\s\.\,\!\?]'
more_than_four = re.split(four_and_more_letters, hw_list)
new_dict = {}
new_work = [word for word in more_than_four if len(word) >= 4]
new_work_set = set(new_work)
for word in new_work_set:
    number = 0
    for key in new_work:
        if key == word:
            number += 1
    new_dict[word] = number
# print(new_dict)

more_dicts = sorted(new_dict.items(), key=lambda val: val[1])

more_dicts.reverse()
print(more_dicts[:10])

# 4. Отберите все ссылки.
# Примечание: Для поиска воспользуйтесь методом compile, в который вы вставите свой шаблон для поиска ссылок в тексте.

pattern_string = "[a-z.A-Z0-9]+\.ru[a-zA-Z0-9/]*"
pattern = re.compile(pattern_string)
pattern_list = pattern.findall(hw_list)

print(pattern_list)

# 5. Ссылки на страницы какого домена встречаются чаще всего? Напоминаем, что доменное имя — часть ссылки до первого
# символа «слеш». Например в ссылке вида travel.mail.ru/travel?id=5 доменным именем является travel.mail.ru. Подсчет
# частоты сделайте по аналогии с заданием 3, но верните только одну самую частую ссылку.

non_pattern_string = "[a-z.A-Z0-9]+\.ru"
pattern_for_switch = re.compile(non_pattern_string)
pattern_list = pattern_for_switch.findall(hw_list)
non_pattern_dict = set(pattern_list)
new_pattern_dict = {}
for word in non_pattern_dict:
    number = 0
    for key in pattern_list:
        if key == word:
            number += 1
    new_pattern_dict[word] = number

more_pattern_dicts = sorted(new_pattern_dict.items(), key=lambda val: val[1])

more_pattern_dicts.reverse()
print(more_pattern_dicts[0])

# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

switch_list = re.sub(pattern, 'Ссылка отобразится после регистрации', hw_list)
print(switch_list)
