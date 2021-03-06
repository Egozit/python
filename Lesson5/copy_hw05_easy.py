import os, re, sys, shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_folder(dir_name):
    try:
        path = os.path.join(os.getcwd(), dir_name)
        os.mkdir(path)
        message = 'Директория {} создана'.format(dir_name)
    except FileExistsError:
        message = 'Directory {} already exists'.format(dir_name)
    finally:
        return message


def del_folder(dir_name):
    try:
        path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(path)
        message = 'Директория {} удалена'.format(dir_name)
    except FileNotFoundError:
        message = 'Directory {} doesnt exist'.format(dir_name)
    finally:
        return message


def listdir():
    list = os.listdir(os.getcwd())
    return list


def copy_dir():
    dir_name = re.search('\/([^\/]+)$', sys.argv[0])[1]
    shutil.copy(dir_name, os.path.join(os.getcwd(), 'copy_' + dir_name))
    if os.path.exists('copy_' + dir_name):
        print('File was copied')


if __name__ == '__main__':
    print('{:*^30}'.format('Задача-1'))

    for itm in range(1, 10):
        print(create_folder('dir_' + str(itm)))

    for itm in range(1, 10):
        print(del_folder('dir_' + str(itm)))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
    print('{:*^30}'.format('Задача-2'))

    list = listdir()
    list1 = [el for el in list if not re.search('(\.[a-z]+)$', el)]
    print('Folders in current directory: {}'.format(list1))
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    print('{:*^30}'.format('Задача-3'))

    copy_dir()
