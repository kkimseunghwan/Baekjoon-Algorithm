#1389
from sys import stdin 

N, M = map(int, stdin.readline().split())
graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
  # A <-> B 연결 설정
  a, b = map(int, stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행 > 
for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      if a == b:
        graph[a][b] = 0
      else:
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

num = min = int(1e9)
# 수행된 결과를 출력
for a in range(1, N + 1):
  max = 0
  for b in range(1, N + 1):
    if graph[a][b] != int(1e9):
      max += graph[a][b]
  if min > max:
    min = max
    num = a
    
print(num)