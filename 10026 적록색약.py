# 10026 적록색약
from sys import stdin
from collections import deque

def Normal(grid, N):
  cnt = 0
  for i in range(N):
    for j in range(N):
      if grid[i][j] != 0:
        DFS(grid, N, i, j)
        cnt += 1
  return cnt

def DFS(grid, N, i, j):
  connect = [ (1,0), (0,1), (-1,0), (0,-1) ]
  color = grid[i][j]
  stack = [ (i,j) ]
  grid[i][j] = 0

  while stack:
    y, x = stack.pop()
    for nx, ny in connect:
      nx, ny = nx + x, ny + y
      if (0 <= nx < N and 0 <= ny < N) and grid[ny][nx] == color:
        stack.append( (ny, nx) )
        grid[ny][nx] = 0


# (1 ≤ N ≤ 100)
N = int(input())
grid = []
for _ in range(N):
  grid.append(list(input()))

RG_grid = []
for i in grid:
  RG_grid.append( [ 'RG' if x in ('R', 'G') else 'B' for x in i ] )

print(Normal(grid, N), Normal(RG_grid, N))
