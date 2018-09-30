# EASY
#
# task 1
#
# import random
#
# num = random.randint(-1000, 1000)
#
# idx = 0
# data = str(num)
# print(data)
#
# while idx < len(data):
#     print(idx, data[idx])
#     idx += 1
#
# Better version
# import random
#
# num = random.randint(-1000, 1000)
# print(num)
#
# for idx, char in enumerate(str(num)):
#     print(idx, char)
#
# task 2
#
# a = input('enter a ')
# b = input('enter b ')
#
# a, b = b, a
#
# print(a, b)
#
# task 3
#
# age = input('enter age ')
#
# message = 'success' if int(age) >= 18 else 'denied'
#
# print(message)
#
# HARD
#
# a = float('infinity')
#
# print(a)
#
# LESSON NUMBER TWO
#
# strings
#
# string1 = ''
# string2 = ""
# string3 = '''
# Hello
# world
# '''
