class Person:
    def __init__(self, name, surname, patronymic):
        self._name = name
        self._surname = surname
        self._patronymic = patronymic

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def patronymic(self):
        return self._patronymic

    def __str__(self):
        # return ' '.join((self._name, self._surname, self._patronymic))
        return f'{self._name} {self._surname} {self._patronymic}'
