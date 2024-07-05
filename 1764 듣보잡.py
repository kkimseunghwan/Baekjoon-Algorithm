from sys import stdin
N, M = map(int, stdin.readline().split())
name_01 = set()
name_02 = set()
for _ in range(N):
  name_01.add(stdin.readline().strip())
for _ in range(M):
  name_02.add(stdin.readline().strip())

newName = name_01 & name_02
newName = sorted(newName)
print(len(newName))
for i in newName:
  print(i)