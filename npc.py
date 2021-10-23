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

    def __init__(self, level):
        name = ['Ghost', 'Goblin', 'Elf']
        self.name = name[random.randint(0, len(name)-1)]
        self.atk = 1 + (level - 1) * 2
        self.hp = 1 + (level - 1) * 2
        self.coin = random.randint(1, 5)

class Boss(Enemy):

    def __init__(self, level):
        self.name = name.generate(type='monster')
        self.atk = 5 + (level - 1) * 2
        self.hp = 5 + (level - 1) * 2
        self.coin = 20

def generate_enemies(level):
    enimies = []
    for i in range(5):
        enimies.append(Enemy(level))
    enimies.append(Boss(level))
    return enimies


if __name__ == '__main__':
    e = generate_enemies()
    print(type(e[0]))
