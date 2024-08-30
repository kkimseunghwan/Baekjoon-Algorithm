from sys import stdin
from collections import deque

def BFS(graph, N, M):
  moving = [ (-1, 0), (0, -1), (1, 0), (0, 1)]
  queue = deque([(0, 0)]) # 시작 정점을 큐에 넣기
  graph[0][0] = 1 # 시작 정점 방문 처리
  
  move_cnt = 1
  while queue: # 큐이 빌 때까지 이 과정을 반복

    for _ in range(len(queue)):
      x, y = queue.popleft() # 큐에서 정점을 하나 꺼내고

      if (x,y) == (N-1, M-1):
        return move_cnt
        
      for nx, ny in moving:
        nx = x + nx
        ny = y + ny
        if (0 <= nx < N and 0 <= ny < M) and graph[nx][ny] == 1:
          queue.append((nx, ny))
          graph[nx][ny] = 0 # 방문 처리
    move_cnt += 1

# N, M(2 ≤ N, M ≤ 100)
N, M = map(int, stdin.readline().split())
maze = []
for _ in range(N):
  maze.append([int(x) for x in stdin.readline().strip()])

print(BFS(maze, N, M))

