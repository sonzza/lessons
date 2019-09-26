# 1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке
# разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить
# в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

import os
import shutil
import datetime
import random


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже существует')
    else:
        shutil.copy(name, new_name)


def change_dir(f_name):
    f_name = os.path.join(os.getcwd(), f_name)
    try:
        os.mkdir(f_name)
    except FileExistsError:
        os.chdir(f_name)


def safe_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def game():
    number = random.randint(1, 100)
    print('Загадайте число от 1 до 100. \n Это число ', number, '?')
    start = 1
    end = 100
    user_input_char = int(input('Выберите ответ: 1. Больше загаданного 2. Меньше загаданного 3. Бинго! '))
    while user_input_char != 3:
        if user_input_char == 2:
            start = number + 1
            number = random.randint(start, end)
            print('Это число ', number, '?')
            user_input_char = int(input('Выберите ответ: 1. Больше загаданного 2. Меньше загаданного 3. Бинго!'))
        elif user_input_char == 1:
            end = number - 1
            number = random.randint(start, end)
            print('Это число  ', number, '?')
            user_input_char = int(input('Выберите ответ: 1. Больше загаданного  2. Меньше загаданного 3. Бинго!'))
    print('Искусственный интеллект умнее всех!')


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_file('new_folder')
    safe_info('текущее время')
