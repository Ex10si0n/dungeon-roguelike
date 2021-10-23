import random
import npc
from maze import generate

class Map:
    def __init__(self):
        self.x, self.y = 5, 5
        self.enemies = npc.generate_enemies()
        self.map = generate(self.x, self.y)
        self.display_enemies()
        self.add_room()
        self.add_enimies(level=1)
        self.add_chest()
        self.add_merchant()
        self.render()
        self.map[1][1] = 's'
        self.map[len(self.map)-2][len(self.map)-2] = 'e'

    def display_enemies(self):
        for i in range(len(self.enemies)):
            print('%d - %s' % (i, self.enemies[i].desc()))
        print()

    def add_room(self):
        room_size = 3
        corner_x = random.randint(0, 3) * 2 + 1
        corner_y = random.randint(0, 3) * 2 + 1
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if (i >= corner_x - 1 and i < corner_x + room_size + 1) and (j >= corner_y - 1 and j < corner_y + room_size + 1):
                    self.map[i][j] = 'W'
                if i in range(corner_x, corner_x + room_size) and j in range(corner_y, corner_y + room_size):
                    self.map[i][j] = 'R'
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if i == 0 or i == len(self.map) - 1 or j == 0 or j == len(self.map) - 1:
                    self.map[i][j] = 'X'
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if i == 0 or i == len(self.map) or j == 0 or j == len(self.map):
                    self.map[i][j] = 'X'
                if self.map[i][j] == 'W':    # find wall
                    if i == corner_x - 1 and j == corner_y - 1: self.map[i][j] = 'X'
                    if i == corner_x - 1 and j == corner_y + room_size: self.map[i][j] = 'X'
                    if i == corner_x + room_size and j == corner_y - 1: self.map[i][j] = 'X'
                    if i == corner_x + room_size and j == corner_y + room_size: self.map[i][j] = 'X'

    def add_enimies(self, level):
        enemies = []
        for e in self.enemies:
            enemies.append(e)

        interval = 0
        no = 0
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if self.map[i][j] == ' ' and i > 1 and j > 1:
                    interval += 1
                    if len(enemies) == 0:
                        break
                    if interval == 4:
                        interval = 0
                        e = enemies.pop()
                        self.map[i][j] = e
                        no += 1

    def add_chest(self):
        pos = random.randint(0, 8)
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if self.map[i][j] == 'R':
                    pos -= 1
                    if pos == 0: self.map[i][j] = 'C'

    def add_merchant(self):
        pos = random.randint(0, 7)
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if self.map[i][j] == 'R':
                    pos -= 1
                    if pos == 0: self.map[i][j] = 'M'


    def display(self):
        for i in self.map:
            for j in i:
                print(j, end=' ')
            print()

    def render(self):
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if self.map[i][j] == 'R':
                    self.map[i][j] = ' '


if __name__ == '__main__':
    m = Map()
    m.display()
