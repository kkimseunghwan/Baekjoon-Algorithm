#11403
from sys import stdin 
INF = int(1e9)
N = int( stdin.readline())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

numLn = []
for _ in range(N):
  numLn.append(list(map(int, stdin.readline().split())))

for a in range(1, N+1):
  for b in range(1, N+1):
    if numLn[a-1][b-1] == 1:
      graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행 > 
for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        
# 수행된 결과를 출력
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()