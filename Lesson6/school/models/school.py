from .person import Person


class Student(Person):
    def __init__(self, name, surname, patronymic, mother, father):
        super(Student, self).__init__(name, surname, patronymic)
        self._mother = mother
        self._father = father

    @property
    def mother(self):
        return str(self._mother)

    @property
    def father(self):
        return str(self._father.name)

    def __str__(self):
        return f'{self._surname} {self._name[0]}. {self._patronymic[0].}'


class Teacher(Person):
    def __init__(self, name, surname, patronymic,subject, klass):
        super(Student, self).__init__(name, surname, patronymic)
        self._klass = klass

    @property
    def subject(self):
        return str(self._subject)

    @property
    def klass(self):
        return str(self._klass)

class SchoolClass:
    def __init__(self, name, *students):
        self._name = name
        self._students = students

    @property
    def name(self):
        return str(self._name)

    @property
    def students(self):
        return str(self._students)

class School:
    def __init__(self, klasses, teachers):
        self._klasses = klasses
        self._teachers = teachers

    @property
    def klasses(self):
        return self._klasses

    @property
    def teachers(self):
        return str(self._teachers)

    def get_klass_students(self, klass_name):
        query = list(
            filter(lambda itm: itm.name == klass_name, self._klasses)
        )
        klass = query[0] if klasses else None

        return klass.students if klass else []


    def get_teacher_students(self, teacher_name):
        query = list(
            filter(lambda itm: itm.name == teacher_name, self._teachers)
        )
        klass = query[0] if klasses else None

        return klass.students if klass else []
