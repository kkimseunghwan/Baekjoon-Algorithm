from sys import stdin
mirrorNum = {1:1, 2:5, 5:2, 8:8}

N, M = map(str, stdin.readline().split())
num = []
for _ in range(int(M)):
  num.append(list(map(int, stdin.readline().split())))
  if N in ('R', 'L'):
    num[-1] = num[-1][::-1]

if N in ('U', 'D'):
  num = num[::-1]

for i in range(len(num)):
  for j in range(len(num[0])):
    print(mirrorNum[num[i][j]] if num[i][j] in mirrorNum else '?', end=' ')
  print()


