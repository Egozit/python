import hw05_easy as easy
import sys, os
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def print_help():
    print("help - получение справки")
    print("open - Перейти в папку")
    print("listdir - Просмотреть содержимое текущей папки")
    print("del - Удалить папку")
    print("create - Создать папку")

# Функция на открытие папки работает только во время выполнения одного вызова
#  в консоли, как сделать ее многоразовой, чтобы программа работала с той
# директорией, что я задаю в последствии, я не знаю
def open_folder(dir_name):
    try:
        os.chdir(os.path.join(os.getcwd(), dir_name))
        message = 'Directory opened'
        print(os.getcwd())
    except FileNotFoundError:
        message = 'File not found'
    finally:
        return message


do = {
    'help': print_help,
    'open': open_folder,
    'listdir': easy.listdir,
    'del': easy.del_folder,
    'create': easy.create_folder
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
        if dir_name:
            print(1)
            print(do[key](dir_name))
        else:
            print(do[key]())
    else:
        print('Wrong key')
