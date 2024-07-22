#10546 배부른마라토너
from sys import stdin
N = int(stdin.readline())
player = {}
for _ in range(N):
  p = stdin.readline().strip()
  if p in player: player[p] += 1
  else: player[p] = 1
for _ in range(N-1):
  player[stdin.readline().strip()] -= 1
for a, b in player.items():
  if b != 0:
    print(a)
    break