 
from sys import stdin

Olymiad = []
medal = {}
for _ in range(int(stdin.readline())):
    country, player, score = map(int, stdin.readline().split())
    Olymiad.append([country, player, score])
    if not (country in medal):
        medal[country] = 0

Olymiad.sort(key=lambda x: (-x[2]))


for i in Olymiad:
  if sum(medal.values()) == 3:
      break
  if medal[i[0]] >= 2:
      continue
  else:
      medal[i[0]] += 1
      print(i[0], i[1])

