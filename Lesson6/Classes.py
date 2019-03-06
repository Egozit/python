# class Student:
#     def __init__(self, name, surname, birth_date, school, class_room):
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         self.school = school
#         self._class_room = {'class_num': int(class_room.split()[0]),
#                                         'class_char': class_room.split()[1]}
#
#     @property
#     def class_room(self):
#         return "{} {}".format(self._class_room['class_num'],
#                                         self._class_room['class_char'])
#
#     def next_class(self):
#         self._class_room['class_num'] += 1
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def set_name(self, new_name):
#         self.name = new_name


# class Teacher:
#     def __init__(self, name, surname, birth_date, school, teach_classes):
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         self.school = school
#         self.teach_classes = list(map(self.convert_class, teach_classes))
#
#     def convert_class(self, class_room):
#         """
#         '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int':
#         <class_int>}
#         """
#         return {'class_num': int(class_room.split()[0]),
#         'class_char': class_room.split()[1]}
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def set_name(self, new_name):
#         self.name = new_name
# Эти Классы описывают два различных объекта.
# Но часть информации у них общая (атрибуты, методы).
# Общую информацию выносим в Класс-предок (родитель):


# class Person:
#     def __init__(self, name, surname, birth_date, school):
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         self.school = school
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def set_name(self, new_name):
#         self.name = new_name
# # Сами классы наследуем
#
#
# class Student(Person):
#     def __init__(self, name, surname, birth_date, school, class_room):
# # Явно вызываем конструктор родительского класса
#         Person.__init__(self, name, surname, birth_date, school)
#     # Добавляем уникальные атрибуты
#         self._class_room = {'class_num': int(class_room.split()[0]),
#         'class_char': class_room.split()[1]}
#     # И уникальные методы
#     @property
#     def class_room(self):
#         return "{} {}".format(self._class_room['class_num'],
#         self._class_room['class_char'])
#     def next_class(self):
#         self._class_room['class_num'] += 1
#
# class Teacher(Person):
#     def __init__(self, name, surname, birth_date, school, teach_classes):
#         Person.__init__(self, name, surname, birth_date, school)
#         self.teach_classes = list(map(self.convert_class, teach_classes))
#     # Уникальный метод Учителя
#     def convert_class(self, class_room):
#         """
#         '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int':
#         <class_int>}
#         """
#         return {'class_num': int(class_room.split()[0]),
#         'class_char': class_room.split()[1]}

# Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
# Инкапсуляция делает некоторые из компонент доступными только внутри класса.


# Исходный класс Студента
class Student:
    def __init__(self, name, surname, birth_date, school, class_room):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self.class_room = class_room

    def next_class(self):
        self.class_room = str(int(self.class_room.split()[0]) + 1) + ' ' + \
                          self.class_room.split()[1]

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


# Далее мы используем класс в многих местах различных программ
students = [Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5 А"),
            Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8 Б"),
            Student("Иван", "Петров", '12.11.1999', "8 гимназия", "4 В"),
            ]
# Учебный год закончился
for student in students:
    student.next_class()

for num, student in enumerate(students, start=1):
    print("{}) {} класс: {}".format(num, student.get_full_name(), student.class_room))


# ... и еще куча кода с использованием Student

# Но потом вы заметили, что реализация метода .next_class() смотрится ну очень плохо
# И чтобы написать хороший код, решили хранить инфо. о классе по-другому

# class Student:
#     def __init__(self, name, surname, birth_date, school, class_room):
#         ...
#         self.class_room = {'class_num': int(class_room.split()[0]),
#                            'class_char': class_room.split()[1]}
#         класс храним в виде словарика {номер класс , буква класса}
#         ...
#     Теперь метод выглядит понятно и легкочитаемо
#     def next_class(self):
#         self.class_room['class_num'] += 1

# Чтобы использовать новую реализацию класса, вам придется переписать кучу готового кода
# Т.к. атрибут class_room - это словарь, а не строка
# Чтобы этого избежать, делаем так:

class Student:
    def __init__(self, name, surname, birth_date, school, class_room):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        # Символ нижнего подчеркивания говорит пользователям класса, что атрибут для внутреннего использования
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # @property - позволяет обращаться к методу, как к атрибуту
    # .class_room() --> .class_room

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


# Старый код работает с новым классом без изменений
print("******После изменения класса*******")
students = [Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5 А"),
            Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8 Б"),
            Student("Иван", "Петров", '12.11.1999', "8 гимназия", "4 В"),
            ]

# Учебный год закончился
for student in students:
    student.next_class()

for num, student in enumerate(students, start=1):
    print("{}) {} класс: {}".format(num, student.get_full_name(), student.class_room))

# В данном примере мы использовали приемы инкапсуляции, чтобы скрыть внутреннюю реализацию класса


# Еще один пример инкапсуляции, с использованием класса Вектор
import math


class Vector:
    """
    Класс для Вектора - направленного отрезка на плоскости
    """

    def __init__(self, coords):
        # Координаты храним в атрибуте __coord (ну захотелось нам так)
        # Два символа подчеркивания __ разрешают доступ к атрибуту только внутри класса
        self.__coords = coords

    @property  # с помощью этого декоратора можем обращаться к атрибуту x --> self.x Или obj.x
    def x(self):
        return self.__coords[0]

    @x.setter  # Позволяет в удобной форме устанавливать атрибут x --> self.x = 10 или obj.x = 10
    def x(self, x):
        self.__coords = x, self.__coords[1]

    @property
    def y(self):
        return self.__coords[1]

    @y.setter
    def y(self, y):
        self.__coords = self.__coords[0], y

    @property
    def len(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @len.setter
    def len(self, value):
        self.x = 10
        self.y = 10

    def as_point(self):
        return self.__coords

    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x, self.y = x, y


v1 = Vector((10, 5))
v2 = Vector((-10, 8))

print('v1.x = ', v1.x)
print('v2.y', v2.y)
# print(v1.__coords) <-- так обратиться нельзя

# Изменение атрибута вызывает метод: def x(self, x) с декоратором @x.setter
v1.x = -21
print('v1.x = ', v1.x)
