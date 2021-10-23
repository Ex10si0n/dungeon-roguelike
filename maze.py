import random

class Config:
    scale_x = 5
    scale_y = 5
    vis = [[0 for col in range(5 + 1)] for row in range(5 + 1)]
    maze = [['X' for col in range(2 * 5 + 1)] for row in range(2 * 5 + 1)]
    sol = [[0 for col in range(2 * 5 + 1)] for row in range(2 * 5 + 1)]
    dir_x = [0, -1, 0, 1]
    dir_y = [1, 0, -1, 0]
    shuf = [0, 1, 2, 3]
    flag = 0
    trac = []
    ans = []

def generate(scale_x, scale_y):
    Config.scale_x, scale_y = 5, 5
    Config.vis = [[0 for col in range(scale_y + 1)] for row in range(scale_x + 1)]
    Config.maze = [['X' for col in range(2 * scale_y + 1)] for row in range(2 * scale_x + 1)]
    Config.sol = [[0 for col in range(2 * scale_y + 1)] for row in range(2 * scale_x + 1)]
    Config.dir_x = [0, -1, 0, 1]
    Config.dir_y = [1, 0, -1, 0]
    Config.shuf = [0, 1, 2, 3]
    Config.flag = 0
    Config.trac = []
    Config.ans = []

    for i in range(1, 2 * Config.scale_x + 1, 2):
	    for j in range(1, 2 * Config.scale_y + 1, 2):
		    Config.maze[i][j] = ' '
	
    gen_maze(0, 0)
    return Config.maze


def gen_maze(now_x, now_y):
	Config.shuf = [0, 1, 2, 3]
	Config.vis[now_x][now_y] = 1
	random.shuffle(Config.shuf)
	for i in Config.shuf:
		new_x, new_y = now_x + Config.dir_x[i], now_y + Config.dir_y[i]
		if new_x < 0 or new_x >= Config.scale_x or new_y < 0 or new_y >= Config.scale_y:
			pass
		else:
			if not Config.vis[new_x][new_y]:
				Config.maze[2 * now_x + 1 + Config.dir_x[i]][2 * now_y + 1 + Config.dir_y[i]] = ' '
				gen_maze(new_x, new_y)
