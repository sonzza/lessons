import os


def add_dir():
    dir_mas = []
    for i in range(1, 10):
        new_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_dir)
        dir_mas.append(new_dir)
    return dir_mas


def del_dir(dir_dir):
    for dir_name in dir_dir:
        os.rmdir(dir_name)


dir_mas = add_dir()
del_dir(dir_mas)
