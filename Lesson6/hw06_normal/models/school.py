from functools import reduce
from person import Person


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
        return str(self._father)

    def __str__(self):
        return f'{self._surname} {self._name[0]}. {self._patronymic[0]}.'


class Teacher(Person):
    def __init__(self, name, surname, patronymic, subject, *klasses):
        super(Teacher, self).__init__(name, surname, patronymic)
        self._subject = subject
        self._klasses = klasses

    @property
    def subject(self):
        return self._subject

    @property
    def klasses(self):
        return self._klasses

    @property
    def students(self):
        return tuple(
            reduce(
                lambda x, y: x + y,
                map(
                    lambda itm: itm.students,
                    self._klasses
                )
            )
        )


class SchoolClass:
    def __init__(self, name, *students):
        self._name = name
        self._students = students

    @property
    def name(self):
        return self._name

    @property
    def students(self):
        return self._students


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

    @property
    def students(self):
        return tuple(
            reduce(
                lambda x, y: x + y,
                map(
                    lambda itm: itm.students,
                    self._klasses
                )
            )
        )

    def get_klass_students(self, klass_name):
        query = tuple(
            filter(lambda itm: itm.name == klass_name, self._klasses)
        )
        klass = query[0] if query else None

        return klass.students if klass else []

    def get_teacher_students(self, teacher_name):
        query = tuple(
            filter(lambda itm: itm.name == teacher_name, self._teachers)
        )
        teacher = query[0] if query else None

        return teacher.students if teacher else []

    def get_student_by_name(self, student_name, student_surname, klass_name):
        query = tuple(
            filter(
                lambda itm: itm.name == student_name and itm.surname ==
                            student_surname,
                self.get_klass_students(klass_name)
            )
        )

        return query[0] if query else None
