
from sys import stdin
from collections import deque

def BFS(grid, l, start, target):
  if start == target:
    return 0
  
  Night_Move = [ (2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, -2), (-1, 2) ]
  grid[start[0]][start[1]] = 1 # 방문 여부 처리
  queue = deque( [start] ) # 시작 노드 저장
  moveCnt = 0 # 나이트 이동 카운트
  
  isEnd = False
  while queue:
    moveCnt += 1
    for _ in range(len(queue)):
      y, x = queue.popleft()
      for ny, nx in Night_Move:
        ny, nx = ny + y, nx + x
        if (0 <= ny < l and 0 <= nx < l) and grid[ny][nx] == 0:
          if (ny, nx) == target: isEnd = True
          else:
            queue.append( (ny, nx) )
            grid[ny][nx] = 1
    if isEnd:
      break

  return moveCnt

T = int(stdin.readline())
for _ in range(T):
  l = int(stdin.readline()) # 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)
  grid = [ [0] * l for _ in range(l) ] # 체스 판.

  s_y, s_x = map(int, stdin.readline().split()) # 나이트가 현재 있는 칸
  t_y, t_x = list(map(int, stdin.readline().split())) # 나이트가 이동하려고 하는 칸
  start_Night = (s_y, s_x)
  tartget_Night = (t_y, t_x)
  print(BFS(grid, l, start_Night, tartget_Night))
