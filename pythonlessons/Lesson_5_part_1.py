# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти
# папки. Проверьте работу функций в этом же модуле.


import os


def add_dir():
    for i in range(1, 10):
        new_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_dir)


def del_dir():
    dir_names = os.listdir()
    for dir_name in dir_names:
        if dir_name.find('dir') != -1:
            dir_func = (os.path.join(os.getcwd(), dir_name))
            os.rmdir(dir_func)


if __name__ == '__main__':
    add_dir()
    del_dir()
