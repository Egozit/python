# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os, sys, shutil


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print('rm <file_name> - удаляет указанный файл ')
    print('cd <full_path or relative_path> - меняет текущую директорию '
          'на указанную')
    print('ls - отображение полного пути текущей директории')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

#может скопировать файл но не может директорию, выдает ошибку PermitionError
def copy_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        shutil.copy(dir_name, os.path.join(os.getcwd(), 'copy_' + dir_name))
        if os.path.exists('copy_' + dir_name):
            message = 'File was copied'
    except TypeError:
        message = 'Wrong type of file'
    except FileNotFoundError:
        message = 'File not found'
    except PermissionError:
        message = 'Permission denied'
    finally:
        print(message)
        return


def remove_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директория {} не найдена'.format(dir_name))
    except OSError:
        try:
            os.remove(dir_path)
            print('директория {} удалена'.format(dir_name))
        except OSError:
            print('директоря {} не пуста'.format(dir_name))

#не знаю как вернуться назад по абсолютному пути
def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.chdir(dir_path)
        print('Directory opened {}'.format(dir_path))
        print(os.getcwd())
    except FileNotFoundError:
        print('File not found')


def full_path():
    print('Полный путь текущей директории: {}'.format(os.getcwd()))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': copy_dir,
    'rm': remove_dir,
    'cd': change_dir,
    'ls': full_path
}

while True:
    code = input('Введите ключ команды (q - exit): ')
    code = code.split(' ')
    key = code[0]
    try:
        dir_name = code[1]
    except IndexError:
        dir_name = None
    if key == 'q':
        break
    if key:
        if do.get(key):
            do[key]()
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")

