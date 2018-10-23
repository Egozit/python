import os, re, sys, shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('{:*^30}'.format('Задача-1'))

# for itm in range(1, 10):
#     try:
#         path = os.path.join(os.getcwd(), 'dir_' + str(itm))
#         os.mkdir(path)
#         print('Директория dir_{} создана'.format(str(itm)))
#     except FileExistsError:
#         pass
#
# for itm in range(1, 10):
#     try:
#         path = os.path.join(os.getcwd(), 'dir_' + str(itm))
#         os.rmdir(path)
#         print('Директория dir_{} удалена'.format(str(itm)))
#     except FileNotFoundError:
#         pass

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('{:*^30}'.format('Задача-2'))

list = os.listdir(os.getcwd())
list1 = [el for el in list if not re.search('(\.[a-z]+)$', el)]
print('Folders in current directory: {}'.format(list1))
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('{:*^30}'.format('Задача-3'))

file_name = re.search('\/([^\/]+)$', sys.argv[0])[1]
shutil.copy(file_name, os.path.join(os.getcwd(), 'copy_' + file_name))