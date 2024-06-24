from sys import stdin
import decimal
N, K = map(int, stdin.readline().split())
game = []
for _ in range(N):
  game.append(list(map(int, stdin.readline().split())))


game.sort(key = lambda x: (-(decimal.Decimal(x[2]) / decimal.Decimal(x[1])), x[1], x[0]))
for i in range(K):
  print(game[i][0])
