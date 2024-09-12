# 1697 숨바꼭질
from sys import stdin
from collections import deque

def BFS(start, end):
  if start == end:
    return 0
  
  grid_len = 100000
  grid = [False] * ( grid_len + 1 )
  grid[start] = True

  cnt = 0
  queue = deque( [start] )


  while queue:
    cnt += 1
    for _ in range(len(queue)):
      X = queue.popleft()

      if X-1 >= 0:
        if X-1 == end: return cnt
        if not grid[X-1]:
          grid[X-1] = True
          queue.append(X-1)

      if X+1 <= grid_len:
        if X+1 == end: return cnt
        if not grid[X+1]:
          grid[X+1] = True
          queue.append(X+1)

      if 2*X <= grid_len:
        if 2*X == end:  return cnt
        if not grid[2*X]:
          grid[2*X] = True
          queue.append(2*X)


            

N, K = map(int, stdin.readline().split())

print(BFS(N, K))





