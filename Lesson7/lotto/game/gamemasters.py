import random
from exceptions import StopGameEvent, ExcludeUser


class GameMaster:
    def __init__(self, *players):
        self._players = list(players)
        self._barrels = list(range(1, 91))

    def next(self):
        print(f'Barrels in the bag {len(self._barrels)}')
        if not self._barrels:
            raise StopGameEvent('No more barrels')
        number = random.choice(self._barrels)
        self._barrels.remove(number)
        for player in self._players:
            try:
                player.render()
                player.next(number)
            except ExcludeUser as evt:
                self._players.remove(evt.target)
                print(evt)
