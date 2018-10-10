
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print("{:*^30}".format("Задача-1"))


def my_round(number, ndigits):
    lst = []
    number = str(number)
    for el in number:
        if el != ".":
            lst.append(int(el))
    if lst[ndigits + 1] >= 5:
        lst[ndigits] = lst[ndigits] + 1
    i = ndigits
    while lst[i] == 10:
        lst[i] = 0
        i -= 1
        lst[i] = lst[i] + 1

    lst[-(len(lst)-1 - ndigits):] = []
    lst[1:1] = '.'
    string = ''
    for el in lst:
        string += str(el)
    return string


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print("{:*^30}".format("Задача-2"))


def lucky_ticket(ticket_number):
    message = "Не счастливый билет"
    lst = []
    ticket_number = str(ticket_number)
    for el in ticket_number:
        lst.append(int(el))
    if sum(lst[:3]) == sum(lst[-3:]):
        message = "Билет счастливый!"
    return message

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
