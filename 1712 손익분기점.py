#1712 손익 분기점
from sys import stdin

A, B, C = map(int, stdin.readline().split())
if B >= C:
  print(-1)
else:
  print(A//(C-B) + 1)
