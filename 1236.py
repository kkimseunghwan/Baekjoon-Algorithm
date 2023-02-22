a, b = map(int, input().split())
cas = []

countX = 0
countY = 0
for i in range(a):
  inputcas = input()
  cas.append(inputcas)
  if inputcas.count("X") == 0:
    countX += 1

for i in range(b):
  c = ""
  for j in range(a):
    c += cas[j][i]
  if c.count("X") == 0:
    countY += 1

print(max(countX, countY))
