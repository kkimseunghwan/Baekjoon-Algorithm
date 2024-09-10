#  빙고

from sys import stdin

def isBingo(grid, x, y):
	bingo = 0
	# 가로
	if all(grid[x]): bingo += 1
		
	# 세로
	for i in range(5):
		if not grid[i][y]: break
	else: bingo += 1

	# X자
	if x == y:
		for i in range(5):
			if not grid[i][i]: break
		else: bingo += 1
	
	if x + y == 4:
		for i in range(5):
			if not grid[i][4 - i]: break
		else: bingo += 1
		
	return bingo

bingo_grid = {}
for i in range(5):
	num = list(map(int, stdin.readline().split()))
	for j in range(5):
		bingo_grid[num[j]] = ( i, j )

bingo_set = [ [False] * 5 for _ in range(5) ]
bingo_num = [ list(map(int, stdin.readline().split())) for _ in range(5) ]

bingoCnt = 0
for i in range(5):
	for j in range(5):
		x, y = bingo_grid[ bingo_num[i][j] ]
		bingo_set[x][y] = True
		# 검사
		bingoCnt += isBingo(bingo_set, x, y)
		if  bingoCnt >= 3:
			print( i*5 + j + 1 )
			exit()



