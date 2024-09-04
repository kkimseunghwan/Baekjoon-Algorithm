
from sys import stdin
from collections import deque

def BFS(grid, N, M):
  find_location = [ (1,0), (0,1), (-1,0), (0,-1) ]
  new_Grid = [ [0] * M for _ in range(N) ]
  moveCount = 1

  start = (0, 0)
  # 시작 지점 탐색
  for i in range(N):
    for j in range(M):
      if grid[i][j] == 2:
        start = ( i, j )
      elif grid[i][j] == 1:
        moveCount += 1

  queue = deque( [start] )
  while queue:
    for _ in range(len(queue)):
      y, x = queue.popleft()
      moveCount -= 1
      for ny, nx in find_location:
        ny = ny + y
        nx = nx + x
        if (0 <= ny < N and 0 <= nx < M) and (ny, nx) != start and new_Grid[ny][nx] == 0 and grid[ny][nx] != 0:
          queue.append( (ny, nx) )
          new_Grid[ny][nx] = new_Grid[y][x] + 1

  # 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치 -1 설정
  if moveCount != 0:
    for i in range(N):
      for j in range(M):
        if new_Grid[i][j] == 0 and grid[i][j] == 1:
          new_Grid[i][j] = -1
  
  new_Grid[start[0]][start[1]] = 0
  return new_Grid

# 지도크기 n과 m. n은 세로, m은 가로
# (2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
N, M = map(int, input().split())
grid = []
for _ in range(N):
  grid.append(list(map(int, input().split())))

for i in BFS(grid, N, M):
  for j in i:
    print(j, end=' ')
  print()




