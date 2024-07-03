
from sys import stdin
import math

M, N= map(int, stdin.readline().split())
numList = list(range(N+1))
for i in range(2, int(math.sqrt(N)) + 1):
  if numList[i]:
    for j in range(i * i, N + 1, i):
        numList[j] = 0
for i in numList:
  if i != 0 and i >= M and i != 1:
    print(i)
