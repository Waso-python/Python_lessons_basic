import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir(user_dir):
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)


def del_dir(user_dir):
    if os.path.exists(user_dir):
        os.removedirs(user_dir)


def list_dir(user_dir):
    for el in os.listdir(user_dir):
        print(el)


def create_dir_user():

    for i in range(8):
        dir_user = os.path.join(os.getcwd(), "{}_{}".format("dir",str(i+1)))
        create_dir(dir_user)
    print("Печатаем список созданных папок")
    list_dir(os.getcwd())


def remove_dir_user():
    for i in range(8):
        dir_user = os.path.join(os.getcwd(), "{}_{}".format("dir", str(i + 1)))
        del_dir(dir_user)
    print("Удалили созданные папки")
    list_dir(os.getcwd())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def only_dir():
    print("Печатаем список только директорий")
    for el in os.listdir(os.getcwd()):
        if os.path.isdir(el):
            print(el)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_cur_script():
    print('Файл текущего скрипта = ', sys.argv)
    cur_file = sys.argv[0]
    new_file = cur_file+".dupl"
    try:
        shutil.copy(cur_file, new_file)
        print("Файл создан")
    except FileExistsError:
        print('Такой файл уже существует')

