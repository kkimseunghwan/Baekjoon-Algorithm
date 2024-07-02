from sys import stdin
N=int(stdin.readline().strip())

ball = 1
for _ in range(N):
  X, Y = map(int, stdin.readline().split())
  if X == ball:
    ball = Y
  elif Y == ball:
    ball = X
print(ball)



