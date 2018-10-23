import libs.my_first_lib as my_lib
import os, sys

#
# print(my_lib.do_something())
# print(my_lib.more_then_one(6))
#
# print('os.getcwd() = ', os.getcwd())
#
# dir_path = os.path.join(os.getcwd(), 'NewDir')
#
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print('File already exists')
#
#
# # Список аргументов запуска скрипта,
# # первым аргументом является полный путь к файлу скрипта
# print('sys.argv = ', sys.argv)
# # Список путей для поиска модулей
# print('sys.path = ', sys.path)
# # Полный путь к интерпретатору
# print('sys.executable = ', sys.executable)
# # Словарь имён загруженных модулей
# print('sys.modules = ', sys.modules)
# # Информация об операционной системе
# print('sys.platform = ', sys.platform)
# while True:
#     key = input("press 'q' to Exit")
#     if key == 'q':
#         sys.exit()
#         # Вызов данной функции мгновенно завершает работу модуля (скрипта)

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


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


do = {
"help": print_help,
"mkdir": make_dir,
"ping": ping
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")