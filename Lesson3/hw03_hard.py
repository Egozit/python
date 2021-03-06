import os


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# fraction = '-4 1/2'

# создадим метод для преобразования дроби вида a b/c в неправильную дробь
def get_fraction_components(fraction):
    if fraction != '0':
        # основываясь на количестве знаков в строке выбираем способ переобразования в неправильную дробь
        # всегда возвращаем кортеж из трех элементов: знак дроби, числитель и знаменатель
        if len(fraction) == 1:
            return 1, int(fraction[0]), 1
        elif len(fraction) == 2:
            return -1, int(fraction[1]), 1
        elif len(fraction) == 3:
            return 1, int(fraction[0]), int(fraction[2])
        elif len(fraction) == 4:
            return -1, int(fraction[1]), int(fraction[3])
        elif len(fraction) == 5:
            return 1, int(fraction[0]) * int(fraction[4]) + int(
                fraction[2]), int(fraction[4])
        elif len(fraction) == 6:
            return -1, int(fraction[1]) * int(fraction[5]) + int(
                fraction[3]), int(fraction[5])
    else:
        return 1, 0, 0


# функция длинной больше 50 строк зачастую называется "божественной функцией" (анти-паттерн "Божественный Объект"). Старайтесь избегать создания подобного рода функций, если это возможно.
def fraction_sum(fr1, fr2):
    # задаем значения переменных по умолчанию
    # итоговый знак дроби
    com_sign = ''
    # итоговая целая яасть дроби
    addiction = 0
    # "общий"" числитель
    com_numenator = 0
    # общий знаменатель
    com_denominator = 0

    # получаем элементы дробей fr1 и fr2
    sign1, fr1_numerator, fr1_denominator = get_fraction_components(fr1)
    sign2, fr2_numerator, fr2_denominator = get_fraction_components(fr2)

    # вычисляем значение "общего"" числителя
    com_numenator = fr1_numerator * fr2_denominator * sign1 + fr2_numerator * fr1_denominator * sign2

    # вычисляем находим общий знаменатель
    com_denominator = fr1_denominator * fr2_denominator

    # если числитель отрицателен, то устанавливает итоговый знак дроби отрицательным и определяем абсолютное значение числителя
    if com_numenator < 0:
        com_numenator = abs(com_numenator)
        com_sign = '-'

    # определяем значение челой части
    if com_denominator:
        addiction = com_numenator // com_denominator

    # вычисляем итоговое значение числителя
    result_numenator = com_numenator - addiction * com_denominator

    # если итоговый числитель не равен нулю, то есть у дроби есть дробная часть
    if result_numenator:
        # определяем итоговое значение знаменателя
        result_denominator = com_denominator
        # сокращаем кратные числитель и знаменатель
        if com_denominator % com_numenator == 0:
            result_denominator //= result_numenator
            result_numenator //= result_numenator
        pass
    else:
        result_denominator = 0

    # формируем вывод в зависимости от есть ли у дроби дробная и\или целая часть
    if not result_numenator:
        return '{s}{ad}'.format(s=com_sign, ad=addiction)
    elif not addiction:
        return '{s}{num}/{den}'.format(s=com_sign, num=result_numenator,
                                       den=result_denominator)
    else:
        return '{s}{ad} {num}/{den}'.format(s=com_sign, ad=addiction,
                                            num=result_numenator,
                                            den=result_denominator)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# задаем постоянные для названий заголовков
NAME_HEADER_NAME = 'Имя'
SURNAME_HEADER_NAME = 'Фамилия'
SALARY_HEADER_NAME = 'Зарплата'

HOURS_NORM_HEADER_NAME = 'Норма_часов'
HOURS_WORKED_HEADER_NAME = 'Отработано'

# задаем постоянные для путей к соответствующим файлам
HOURS_OF_FILE_PATH = 'data/hours_of'
WORKERS_FILE_PATH = 'data/workers'

def get_dict_from_file(path):
    data_list = list()
    with open(path, 'r', encoding='UTF-8') as file:
        file_query = file.readlines()
        headers_str = file_query.pop(0).split(' ')
        headers = list(filter(lambda x: x != '', headers_str))
        for line in file_query:
            data_dict = dict()
            data_str = line.split(' ')
            data = list(filter(lambda f: f != '', data_str))
            for idx, header in enumerate(headers):
                header = header.replace('\n', '')
                if idx < len(data):
                    data_dict[header] = data[idx].replace('\n', '')
            data_list.append(data_dict)
        return data_list


def get_salary_by_name(name, surname, hours, workers):
    worker_query = list(filter(lambda w: w[NAME_HEADER_NAME] == name and w[
        SURNAME_HEADER_NAME] == surname, workers))
    hours_query = list(filter(lambda h: h[NAME_HEADER_NAME] == name and h[
        SURNAME_HEADER_NAME] == surname, hours))

    if worker_query and hours_query:
        worker = worker_query[0]
        worker_hours = hours_query[0]
        total_salary = int(worker[SALARY_HEADER_NAME])
        hours_worked = int(worker_hours[HOURS_WORKED_HEADER_NAME])
        hours_norm = int(worker[HOURS_NORM_HEADER_NAME])

        salary_per_hour = total_salary / hours_norm
        return total_salary + salary_per_hour * (hours_worked - hours_norm)

hours = get_dict_from_file(HOURS_OF_FILE_PATH)
workers = get_dict_from_file(WORKERS_FILE_PATH)

for itm in get_dict_from_file(HOURS_OF_FILE_PATH):
    name = itm[NAME_HEADER_NAME]
    surname = itm[SURNAME_HEADER_NAME]
    print(name, surname, ':', get_salary_by_name(name, surname, hours, workers))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые
# файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


FRUITS_FILE_PATH = 'data/fruits.txt'

letters = list(map(chr, range(ord('А'), ord('Я') + 1)))

fruits = list()

with open(FRUITS_FILE_PATH, 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        if line != '\n':
            fruits.append(line.replace('\n', ''))

for let in letters:
    file_name = 'data/fruits/fruits_%s' % let
    with open(file_name, 'w', encoding='UTF-8') as file:
        for fruit in filter(lambda f: f.startswith(let), fruits):
            file.write(fruit + '\n')
