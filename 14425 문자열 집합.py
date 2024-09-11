
from sys import stdin

N, M = map(int, stdin.readline().split())

cnt = 0
S = set()
for _ in range(N):
    S.add( stdin.readline().strip() )
for _ in range(M):
    if stdin.readline().strip() in S:
        cnt += 1
print(cnt)