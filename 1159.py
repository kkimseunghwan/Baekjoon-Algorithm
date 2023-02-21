case = int(input())

player = [input() for _ in range(case) ]

for i in range(len(player)):
  player[i] = player[i][0]

select = []
for i in set(player):
  if player.count(i) >= 5:
    select.append(i)

if len(select) <= 0:
  print("PREDAJA")
else:
  select.sort()
  for i in select:
    print(i, end='')


