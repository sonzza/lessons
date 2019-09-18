import os
import sys

from core import delete_file, safe_info, create_folder, create_file, copy_file, get_list, change_dir, game

safe_info('старт')

command = sys.argv[1]
if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название папки')
    else:
        create_folder(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('отсутствует название файла/папки для копирования или название нового файла/папки')
    else:
        copy_file(name, new_name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название папки')
    else:
        delete_file(name)
elif command == 'change_dir':
    name = sys.argv[2]
    change_dir(name)
    print(os.getcwd())
elif command == 'game':
    game()
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('copy - копирование файла или папки')
    print('delete - удаление файла или папки')
    print('change_dir - смена директории')

safe_info('конец')
