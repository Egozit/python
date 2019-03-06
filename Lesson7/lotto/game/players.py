import random
from exceptions import ExcludeUser, StopGameEvent


class Player:
    def __init__(self, name):
        self._name = name
        self._numbers = list(random.sample(range(1, 91), 15))
        self._cart = self._numbers.copy()

    def render(self):
        print('{blank:->15} {name} {blank:-<15}'.format
              (blank='', name=self._name))

        prev_idx = 0
        for idx in [5, 10, 15]:
            render_list = [
                '{: <2}'.format(itm)
                for itm in self._cart[prev_idx:idx]
            ]
            line = ' '.join(render_list)
            prev_idx = idx
            print(line)

    def next(self, number):
        answer = input(f'Cross number {number}')

        if answer == 'y' and not number in self._numbers:
            raise ExcludeUser(self, 'You lose!')

        if answer == 'n' and number in self._numbers:
            raise ExcludeUser(self, 'You lose!')

        if answer == 'y':
            idx = self._numbers.index(number)
            self._numbers.pop(idx)
            self._cart.pop(idx)
            self._cart.insert(idx, 'x')

        if len(self._numbers) <= 0:
            raise StopGameEvent(f'{self._name} has won!')


class BotPlayer(Player):
    def __init__(self):
        Player.__init__(self, 'AI')

    def next(self, number):
        if number in self._numbers:
            idx = self._numbers.index(number)
            self._numbers.pop(idx)
            self._cart.pop(idx)
            self._cart.insert(idx, 'x')

        if len(self._numbers) <= 0:
            raise StopGameEvent(f'{self._name} has won!')
