import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game2 import game2
from game import game

save_info('Начало')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()

    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            change_dir(name)


    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print("Отсутствует название файла")
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название удаляемой папки или файла')
        else:
            delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название старой и новой папки ли файла')
        else:
            new_name = sys.argv[3]
            copy_file(name, new_name)

    elif command == 'game':
        game()
    elif command == 'game2':
        game2()
    elif command == 'help':
        print('помощь\n'
              'create_file -  Создание нового файла\n'
              'create_folder - Создание новой папки\n'
              'delete - Удаление папки или файла\n'
              'copy - Копирование файла или папки\n'
              'game - Запуск игры угадай число\n'
              'game2- Запуск игры угадай число наобарот\n')
    save_info("Конец")
