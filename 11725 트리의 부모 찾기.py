
# from collections import deque
# from sys import stdin


# def BFS(graph, N):
#     queue = deque([1]) # tree root 1
    
#     visit = [False] * (N+1)
#     visit[1] = True

#     rootInfo = [0] * (N+1)

#     while queue:
#         node = queue.popleft()
#         for x, y in graph:
#             if (x == node) and not visit[y]:
#                 visit[y] = True
#                 rootInfo[y] = x
#                 queue.append(y)
#             elif (y == node) and not visit[x]:
#                 visit[x] = True
#                 rootInfo[x] = y
#                 queue.append(x)

#     return rootInfo[2:]

# N = int(stdin.readline()) #  N (2 ≤ N ≤ 100,000)
# tree = []
# for _ in range(N-1):
#     tree.append(tuple(map(int, stdin.readline().split())))

# for root in BFS(tree, N):
#     print(root)







from collections import deque
from sys import stdin


def BFS(graph, N):
    
    visit = [False] * (N+1)
    visit[1] = True

    rootInfo = [0] * (N+1)

    for i in range(1, N+1):
        for j in graph[i]:
            if visit[i]:
                






    return rootInfo[2:]

N = int(stdin.readline()) #  N (2 ≤ N ≤ 100,000)
tree = dict()
for _ in range(N-1):
    x, y = map(int, stdin.readline().split())
    
    if x not in tree: tree[x] = [y]
    else: tree[x].append(y)

    if y not in tree: tree[y] = [x]
    else: tree[y].append(x)

print(tree)

