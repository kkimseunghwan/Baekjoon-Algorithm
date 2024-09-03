# 11724 연결 요소의 개수
from sys import stdin 
from collections import deque

def BFS(graph, start, visit):
  queue = deque([start]) # 시작 값,
  visit[start] = True

  while queue:
    v = queue.popleft()
    for i in graph[v]: # O(M) M 최대 : 499,500 
      if not visit[i]: # 미방문 시, queue에 추가 및 방문처리
        queue.append(i)
        visit[i] = True

def FindConnectGraph(graph, N):
  visit = [False] * (N+1)
  count = 0
  for i in range(1, N+1):
    if not visit[i]:
      BFS(graph, i, visit)
      count += 1
  return count

# (1 ≤ N(정점) ≤ 1,000, 0 ≤ M(간선) ≤ N×(N-1)/2)
N, M = map(int, stdin.readline().split()) 
graph = [ [] for _ in range(N+1)]
for _ in range(M): # O(M) M 최대 : 499,500
  a, b = map(int, stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

print(FindConnectGraph(graph, N))

