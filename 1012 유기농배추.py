from sys import stdin

def CountCabbage(grid, M, N):
  worm_cnt = 0
  # 배추 군집 시작 좌표를 탐색
  for i in range(N):
    for j in range(M):
      if grid[i][j] == 1:
        # 배추를 찾음. 연결되어있는 모든 배추를 탐색 후 방문표시
        DFS(grid, M, N, j, i)
        worm_cnt += 1

  return worm_cnt
  

def DFS(graph, M, N, x, y):
  worm_move = [ (1,0), (0,1), (-1,0), (0,-1)]
  stack = [ (y, x) ]
  graph[y][x] = -1  # 현재 배추 위치 방문 표시

  # 시작 배추와 연결된 모든 배추들을 탐색 후 방문 표시.
  while stack:
    y, x = stack.pop()

    for a, b in worm_move:
        nx = x + a
        ny = y + b
        if (0 <= nx < M and 0 <= ny < N) and graph[ny][nx] == 1:
          graph[ny][nx] = -1  # 방문 표시
          stack.append( (ny, nx) )


T = int(stdin.readline())

for _ in range(T):
  # 가로 M(1 ≤ M ≤ 50), 세로 N(1 ≤ N ≤ 50), 배추 개수 K(1 ≤ K ≤ 2500)
  M, N, K = map(int, stdin.readline().split())
  Cabbage = [ [0] * M for _ in range(N) ]
    
  for _ in range(K):
    # 배추 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
    x, y = map(int, stdin.readline().split())
    Cabbage[y][x] = 1

  print(CountCabbage(Cabbage, M, N))

