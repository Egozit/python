# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они
#  получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

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
