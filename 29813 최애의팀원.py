from sys import stdin
from collections import deque

N = int(stdin.readline())
std = {}
stdList = []
for _ in range(N):
  name, num = map(str, stdin.readline().split())
  stdList.append(name)
  std[name] = int(num)

stdList = deque(stdList)

while len(stdList) > 1:
  X = std[stdList.popleft()]
  if len(stdList) < X: X = X % len(stdList)

  if X == 0:
    stdList.remove(stdList[-1])
    continue
  
  if X > 1:
    for i in range(0, X-1):
      stdList.append(stdList.popleft())
  
  stdList.popleft()

print(stdList[0])