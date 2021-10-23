import pyglet
import os
from pyglet.window import key
from map import *
from npc import *


class Player:
    hp = 20
    atk = 4
    coin = 0
    player_x = 1
    player_y = 1
    level = 1
    axe = 5
    m = Map(1)
    msg = ''
    dmg = ''

def next_level():
    m = Map(Player.level)
    m.display()
    Player.m = m
    Player.msg = ''
    Player.dmg = ''

def display_minimap():
    try:
        # UNIX
        os.system('clear')
    except:
        # Windows
        os.system('cls')
    Player.m.display_enemies()
    for i in range(len(Player.m.map)):
        for j in range(len(Player.m.map)):
            if j == Player.player_x and i == Player.player_y:
                print('A', end=' ')
            else:
                print(Player.m.map[j][i], end=' ')
        print()

window = pyglet.window.Window()
hp = pyglet.text.Label('HP: ' + str(Player.hp),
                          font_name='Arial',
                          font_size=12,
                          x=window.width - 100, y=window.height - 60)

atk = pyglet.text.Label('ATK: ' + str(Player.atk),
                          font_name='Arial',
                          font_size=12,
                          x=window.width - 100, y=window.height - 80)

coin = pyglet.text.Label('COIN: ' + str(Player.coin),
                          font_name='Arial',
                          font_size=12,
                          x=window.width - 100, y=window.height - 100)

axe = pyglet.text.Label('AXE: ' + str(Player.axe),
                          font_name='Arial',
                          font_size=12,
                          x=window.width - 100, y=window.height - 120)

msg = pyglet.text.Label('',
                          font_name='Arial',
                          font_size=12,
                          color=(0, 255, 0, 255),
                          x=window.width - 200, y=window.height - 150)

dmg = pyglet.text.Label('',
                          font_name='Arial',
                          font_size=12,
                          color=(255, 0, 0, 255),
                          # x=window.width - 200, y=window.height - 170)
                          x=5, y=5)

level = pyglet.text.Label('LEVEL: ' + str(Player.level),
                          font_name='Arial',
                          font_size=12,
                          x=window.width - 100, y=window.height - 20)

king = pyglet.resource.image('assets/king.png')
wall = pyglet.resource.image('assets/wall.png')
start = pyglet.resource.image('assets/start.png')
end = pyglet.resource.image('assets/end.png')
chest = pyglet.resource.image('assets/chest.png')
woodenwall = pyglet.resource.image('assets/woodenwall.png')
goblin = pyglet.resource.image('assets/goblin.png')
elf = pyglet.resource.image('assets/elf.png')
ghost = pyglet.resource.image('assets/ghost.png')
boss = pyglet.resource.image('assets/boss.png')
merchant = pyglet.resource.image('assets/merchant.png')

size = len(Player.m.map) * 40

@window.event
def on_key_press(symbol, modifiers):
    try:
        if symbol == key.W and Player.m.map[Player.player_x][Player.player_y - 1] not in (['X', 'W'] if Player.axe == 0 else ['X']):
            Player.player_y -= 1
        if symbol == key.A and Player.m.map[Player.player_x - 1][Player.player_y] not in (['X', 'W'] if Player.axe == 0 else ['X']):
            Player.player_x -= 1
        if symbol == key.S and Player.m.map[Player.player_x][Player.player_y + 1] not in (['X', 'W'] if Player.axe == 0 else ['X']):
            Player.player_y += 1
        if symbol == key.D and Player.m.map[Player.player_x + 1][Player.player_y] not in (['X', 'W'] if Player.axe == 0 else ['X']):
            Player.player_x += 1

        if Player.m.map[Player.player_x][Player.player_y] == 'W' and Player.axe > 0:
            Player.m.map[Player.player_x][Player.player_y] = ' '
            Player.axe -= 1

        if Player.m.map[Player.player_x][Player.player_y] == 'C':
            selection = random.randint(0, 2)

            if selection == 0:
                value = random.randint(1, 4)
                Player.atk += value
                Player.msg = "ATK enhanced!  +" + str(value)

            if selection == 1:
                value = random.randint(3, 5)
                Player.hp += value
                Player.msg = "HP enhanced!  +" + str(value)

            if selection == 2:
                value = random.randint(1, 10)
                Player.coin += value
                Player.msg = "Coin gained!  +" + str(value)

            Player.m.map[Player.player_x][Player.player_y] = ' '

        if Player.m.map[Player.player_x][Player.player_y] == 'e' and symbol == key.ENTER:
            Player.level += 1
            Player.player_x = 1
            Player.player_y = 1
            next_level()
        try:
            if Player.m.map[Player.player_x][Player.player_y].name in ['Ghost','Goblin', 'Elf']:
                enemy = Player.m.map[Player.player_x][Player.player_y]
                enemy.hp -= Player.atk
                Player.hp -= enemy.atk
                Player.dmg = 'Attacked by ' + enemy.name + '(-%d)' % enemy.atk
                if enemy.hp <= 0:
                    Player.m.map[Player.player_x][Player.player_y] = ' '
                    Player.coin += enemy.coin
                    Player.msg = 'Defeat '+ enemy.name
            else:
                boss = Player.m.map[Player.player_x][Player.player_y]
                boss.hp -= Player.atk
                Player.hp -= boss.atk
                Player.dmg = 'Attacked by ' + boss.name + '(-%d)' % boss.atk
                if boss.hp <= 0:
                    Player.m.map[Player.player_x][Player.player_y] = ' '
                    Player.coin += boss.coin
                    Player.msg = 'Defeat '+ boss.name
        except:
            pass
    except:
        pass
    display_minimap()


@window.event
def on_draw():
    try:
        window.clear()
        hp.text = 'HP: ' + str(Player.hp)
        hp.draw()
        atk.text = 'ATK: ' + str(Player.atk)
        atk.draw()
        coin.text = 'COIN: ' + str(Player.coin)
        coin.draw()
        axe.text = 'AXE: ' + str(Player.axe)
        axe.draw()
        msg.text = Player.msg
        msg.draw()
        dmg.text = Player.dmg
        dmg.draw()
        level.text = 'LEVEL: ' + str(Player.level)
        level.draw()
        px = Player.player_x * 40
        py = size - Player.player_y * 40
        king.blit(px, py)
        for i in range(len(Player.m.map)):
            for j in range(len(Player.m.map)):
                elm = Player.m.map[i][j]
                x = i * 40
                y = size - j * 40
                try:
                    if elm.name == 'Ghost':
                        ghost.blit(x, y)
                    elif elm.name == 'Goblin':
                        goblin.blit(x, y)
                    elif elm.name == 'Elf':
                        elf.blit(x, y)
                    else:
                        boss.blit(x, y)
                except:
                    if elm == 'X':
                        wall.blit(x, y)
                    if elm == 'W':
                        woodenwall.blit(x, y)
                    if elm == 'C':
                        chest.blit(x, y)
                    if elm == 'e':
                        end.blit(x, y)
                    if elm == 'M':
                        merchant.blit(x, y)
    except:
        pass


    

pyglet.app.run()
