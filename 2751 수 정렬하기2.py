from sys import stdin

N = int(stdin.readline().strip())
nl = []
for _ in range(N):
  nl.append(int(stdin.readline().strip()))

nl.sort()
for i in nl:
  print(i)
