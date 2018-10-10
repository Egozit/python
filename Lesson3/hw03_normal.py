# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("{:*^30}".format("Задача-1"))


def fibonacci(n, m):
    lst = [1, 1]
    i = 1
    while True:
        lst.append(lst[i] + lst[i-1])
        i += 1
        if lst[i] == int(n):
            idx_n = i
        if lst[i] == int(m):
            break
    return lst[idx_n:]


n = input("Введите первое значение: ")
m = input("Введите второе значение: ")
print(fibonacci(n, m))
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("{:*^30}".format("Задача-2"))


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
             origin_list[i], origin_list[i + 1] = origin_list[i + 1], \
                                                   origin_list[i]
        n += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("{:*^30}".format("Задача-3"))


def my_filter(func, list):
    list2 = []
    for x in list:
        if func(x):
            list2.append(x)
    list = list2
    return list


func = lambda x: x < 5
list = [2, 5, 10, 20, -4, 27, 3]
print("Первоначальный список: {}".format(list))
print("Конечный список, сортировка по правилу x < 5 : {}".format(my_filter(
    func,
                                                                   list)))
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("{:*^30}".format("Задача-4"))


def check_paral(A1, A2, A3, A4):
    message = 'Это НЕ параллелограмм'

    def check_coord(A1, A2, A3, A4):
        if A2[0] - A1[0] == A4[0] - A3[0] and A2[1] - A1[1] == \
                      A4[1] - A3[1]:
            return True
    if check_coord(A1, A2, A3, A4) or check_coord(A1, A2, A4, A3) or \
            check_coord(A1, A3, A4, A2) or check_coord(A1, A3, A2, A4) or \
            check_coord(A1, A4, A3, A2) or check_coord(A1, A4, A2, A3):
        message = 'Это параллелограмм'
    return message


A1 = (-4, -2)
A2 = (-3, 2)
A3 = (7, -1)
A4 = (6, -5)

print(check_paral(A1, A2, A3, A4))
