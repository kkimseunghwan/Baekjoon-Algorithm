from sys import stdin
from collections import deque

def BFS(graph, N):
    Corona = set()
    visited = [False] * (N + 1)
    queue = deque([1])
    visited[1] = True

    while queue:
        node = queue.popleft()
        for x, y in graph:
            if (x == node and not visited[y]):
                queue.append(y)
                Corona.add(y)
                visited[y] = True
            elif (y == node and not visited[x]):
                queue.append(x)
                Corona.add(x)
                visited[x] = True
    return Corona


N = int(stdin.readline())
M = int(stdin.readline())

connect = []
for _ in range(M):
    x, y = stdin.readline().split()
    connect.append((int(x), int(y)))

print(len(BFS(connect, N)))
