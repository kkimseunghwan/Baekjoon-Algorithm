
from sys import stdin

N = int(stdin.readline())

score = []
for _ in range(N):
	score.append(list(map(str, stdin.readline().split())))

score.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in score:
	print(i[0])
