from collections import deque
from sys import stdin

M, N, H = map(int, stdin.readline().split())
plane = []
for _ in range(H):
  tomto = []
  for _ in range(N):
    tomto.append(list(map(int, stdin.readline().split())))
  plane.append(tomto)


def BFS(plane, M, N, H):
  tomato_make = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
  node = deque()
  cnt = 0
  days = -1

  # 초기 정점 큐에 저장 및 방문이 필요한 정점의 개수 저장
  for h in range(H):
    for i in range(N):
      for j in range(M):
        if plane[h][i][j] == 1:
          node.append((h, i, j))
        elif plane[h][i][j] == 0:
          cnt += 1
  
  # 이동이 필요한 정점의 개수가 없을 경우.
  if cnt == 0:
    return 0
    
  while node:
    for _ in range(len(node)):
      h, x, y = node.popleft()
      for a,b,c in tomato_make:
        nx, ny, nh = a+x, b+y, c+h
        if (0 <= nx < N and 0 <= ny < M and 0 <= nh < H) and plane[nh][nx][ny] == 0:
          plane[nh][nx][ny] = 1
          node.append((nh, nx,ny))
          cnt -= 1
    days += 1
  
  if cnt == 0: 
    return days
  else:
    return -1


print(BFS(plane, M, N, H))
