from person import Person
from school import (
    Student, Teacher, SchoolClass, School
)

klass = SchoolClass(
    '7a',
    Student(
        'a', 'b', 'p',
        Person('a', 'b', 'p'),
        Person('a', 'b', 'p')
    )
)

teacher = (
    Teacher(
        'a', 'b', 'p',
        'math', klass
    ),
)

klasses = (klass,)

school = School(klasses, teacher)

print(school.get_klass_students('7a'))
print(Student.mother)
print(school.get_teacher_students('a'))
