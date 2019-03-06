from gamemasters import GameMaster
from players import Player, BotPlayer
from exceptions import StopGameEvent

user1 = Player('Player1')
bot1 = BotPlayer()

gm = GameMaster(user1, bot1)

while True:
    try:
        gm.next()
    except StopGameEvent as evt:
        print(evt)
        break
