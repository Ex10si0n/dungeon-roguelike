import random

import name

class NPC:

    name = None
    hp = 0
    atk = 0
    coin = 0

    def desc(self):
        return '%s (ATK: %d  HP: %d) [%d]' % (self.name, self.atk, self.hp, self.coin)

    def __str__(self):
        return self.name[0]

class Enemy(NPC):

    def __init__(self):
        name = ['Ghost', 'Goblin', 'Elf']
        self.name = name[random.randint(0, len(name)-1)]
        self.atk = 1
        self.hp = 1
        self.coin = random.randint(1, 5)

class Boss(Enemy):

    def __init__(self):
        self.name = name.generate(type='monster')
        self.atk = 5
        self.hp = 5
        self.coin = 20

def generate_enemies():
    enimies = []
    for i in range(5):
        enimies.append(Enemy())
    enimies.append(Boss())
    return enimies


if __name__ == '__main__':
    pass