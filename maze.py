import random

scale_x, scale_y = 5, 5
vis = [[0 for col in range(scale_y + 1)] for row in range(scale_x + 1)]
maze = [['X' for col in range(2 * scale_y + 1)] for row in range(2 * scale_x + 1)]
sol = [[0 for col in range(2 * scale_y + 1)] for row in range(2 * scale_x + 1)]
dir_x = [0, -1, 0, 1]
dir_y = [1, 0, -1, 0]
shuf = [0, 1, 2, 3]
flag = 0
trac = []
ans = []

def generate(scale_x, scale_y):
	for i in range(1, 2 * scale_x + 1, 2):
		for j in range(1, 2 * scale_y + 1, 2):
			maze[i][j] = ' '
	gen_maze(0, 0)
	return maze


def gen_maze(now_x, now_y):
	shuf = [0, 1, 2, 3]
	vis[now_x][now_y] = 1
	random.shuffle(shuf)
	for i in shuf:
		new_x, new_y = now_x + dir_x[i], now_y + dir_y[i]
		if new_x < 0 or new_x >= scale_x or new_y < 0 or new_y >= scale_y:
			pass
		else:
			if not vis[new_x][new_y]:
				maze[2 * now_x + 1 + dir_x[i]][2 * now_y + 1 + dir_y[i]] = ' '
				gen_maze(new_x, new_y)
