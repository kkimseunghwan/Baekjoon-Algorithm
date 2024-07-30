#21736 현내기는 친구가 필요해
from sys import stdin
N, M = map(int, stdin.readline().split())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
campus, q = [], []
answer = 0

for _ in range(N):
  campus.append(list(stdin.readline().strip()))

for i in range(N):
  for j in range(M):
    if campus[i][j] == 'I':
      q.append((i, j))

while q:
  for _ in range(len(q)):
    x, y = q.pop(0)
    for a, b in directions:
      nx, ny = x+a, y+b
      if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X':
        if campus[nx][ny] == 'P':
          answer += 1
        campus[nx][ny] = 'X'
        q.append((nx, ny))
      
if answer == 0:
  print("TT")
else:
  print(answer)
      