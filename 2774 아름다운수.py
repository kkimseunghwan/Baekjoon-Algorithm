from sys import stdin
T = int(stdin.readline().strip())
for _ in range(T):
  nl = []
  num = stdin.readline().strip()
  for i in num:
    if i not in nl:
      nl.append(i)
  print(len(nl))

