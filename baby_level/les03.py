
import os
import psutil
import sys
import platform
import shutil

def duplicate_file(filename):
    if os.path.isfile(filename):
                newfile = filename + '.dupl'
                shutil.copy(filename, newfile)
                if os.path.exists(newfile):
                    print("Файл ", newfile, " был успешно создан")
                else:
                    print("Возникла ошибка")

def sys_info():
    print("Отлично, за работу!")
    print("Я умею: ")
    print(" [1] - имя текущей директории")
    print(" [2] - выведу название платформы ОС")
    print(" [4] - покажу количество CPU")
    print(" [5] - выведу логин пользователя")
    print(" [3] - выведу список процессов")
    print(" [6] - кодировка файловой системы")
    print(" [7] - дублирование файлов текущей директории")
    print(" [8] - дублирование указанного файла")
    print(" [9] - удаление дубликатов в директории")

answer = ''

while answer != 'q':
    answer = input("Хотите поработать? (Y/N/q)")
    if answer == "Y":
        sys_info()
        do = int(input("Укажите номер действия: "))
        
        if do == 1:
            print(os.getcwd())
        elif do == 2:
            print(platform.system())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print(psutil.cpu_count())
        elif do == 5:
            print(os.getlogin())
        elif do == 6:
            print(sys.getfilesystemencoding())
        elif do == 7:
            print("=Дублирование файлов директории=")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif do == 8:
            print("=дублирование указанного файла=")
            filename = input("укажите файл: ")
            duplicate_file(filename)
        elif do == 9:
            print("= удаление дубликатов в директории=")
            dirname = input("Укажите имя директории: ")
            file_list = os.listdir(dirname)
            # i = 0
            # while i < len(file_list):
            for f in file_list:
                fullname = os.path.join(dirname, f)
                if fullname.endswith(".dupl"):
                    os.remove(fullname)
                i += 1
        else:
            pass
            
    elif answer == "N":
        print("Прощайте!")
    else:
        print("Неизвестный ответ!")
        