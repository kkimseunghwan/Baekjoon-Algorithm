a = int(input())

for i in range(a-1, -1, -1):
  for j in range(0,i):
    print(" ", end='')
  for k in range(i, a):
    print("*", end='')
  print()
