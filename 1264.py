gather = ['A', 'E', 'I', 'O', 'U']

while True:
  a = input()
  if a == "#": break
  cnt = 0
  for i in gather:
    cnt += a.upper().count(i)
  print(cnt)


