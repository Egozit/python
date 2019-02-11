import os, re
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


class Worker:
    def __init__(self, line):
        name, surname, salary, position, norma = line.split()

        self.fullname = name + ' ' + surname
        self.salary = float(salary)
        self.position = position
        self.norma = float(norma)
        # self.worked = float(worked)
        self.pay_ratio = self.salary / self.norma

    def calculate_salary(self):
        if self.worked > self.norma:
            payout_salary = self.pay_ratio * 2 * (self.worked - self.norma) \
                            + self.salary
        elif self.worked < self.norma:
            payout_salary = - self.pay_ratio * (self.norma - self.worked) \
                            + self.salary
        else:
            payout_salary = self.salary
        return payout_salary


workers = []
with open(os.path.join('data', 'workers'), 'r', encoding='UTF-8') as f, \
        open(os.path.join('data', 'hours_of'), 'r', encoding='UTF-8') as h:
    quary = f.readlines()
    hours = h.readlines()
    for line in quary:
        res = re.findall('(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)', line)
        if res:
            workers.append(Worker(line))

    for hour in hours:
        res = re.findall('(\S+)\s+(\S+)\s+(\d+)', hour)
        if res:
            name, surname, worked = res[0]
            worker = [x for x in workers if x.fullname == name + ' ' +
                      surname][0]
            worker.worked = float(worked)

for worker in workers:
    print(worker.fullname, ':', worker.calculate_salary())
