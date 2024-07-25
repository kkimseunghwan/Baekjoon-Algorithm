from sys import stdin
N, M = map(int, stdin.readline().split())
files = []
extension = set()
for _ in range(N):
  files.append(stdin.readline().strip().split('.'))
for _ in range(M):
  extension.add(stdin.readline().strip())

files.sort(key = lambda x : (x[0], -(x[1] in extension), x[1]))

for i in files:
  print('.'.join(i))

