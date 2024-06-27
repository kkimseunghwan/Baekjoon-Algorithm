from sys import stdin

N = int(stdin.readline().strip())
nl = []
for _ in range(N):
  nl.append(list(map(int, stdin.readline().split())))

nl.sort(key = lambda x: (x[1], x[0]))
for i in nl:
  print(i[0], i[1])
