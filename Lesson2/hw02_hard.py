# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print("{:*^30}".format("Задача-1"))

index_x = equation.find('x')

k = float((equation[equation.find("=") + 1:equation.find("x")]))
if equation.find('+', index_x) != -1:
    b = float((equation[equation.find("+", index_x) + 1:]))
elif equation.find('-', index_x) != -1:
    b = (equation[equation.find("-", index_x) + 1:])
    b = -float(b)

y = k * x + b
print("y = ", y)
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.+-
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне
# от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
print("{:*^30}".format("Задача-2"))

day = date[:2]
month = date[3:5]
year = date[6:]
if day.isdigit() and len(day) == 2 and len(month) == 2 and len(year) == 4 and 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1 <= int(year) <= 9999:
    if int(month) % 2 == 0 and int(day) == 31 and int(month) < 8:
        print("В этом месяце меньше дней")
    elif int(month) % 2 != 0 and int(day) == 31 and int(month) >= 8:
        print("В этом месяце меньше дней")
    else:
        print("Дата корректна!")
else:
    print("Ошибка при вводе даты!")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты
# N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева
# на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
print("{:*^30}".format("Задача-3"))
N =input("В какую комнату поедем?")

list = []
i = 1
num = 0

while i < int(N) + 1 and num <= int(N):
    list_i = []
    j = 0
    while j < i * i:
        j += 1
        num += 1
        list_i.append(num)
        if j % i == 0:
            list.append(list_i)
            list_i = []
    i += 1

print(list)

i = 0
while i < len(list):
    if int(N) in list[i]:
        print(i + 1, "этаж", list[i].index(int(N)) + 1, "комната")
    i += 1
