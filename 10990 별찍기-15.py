from sys import stdin
N = int(stdin.readline())
for i in range(1, N+1):
  for k in range(N-i):
    print(" ", end='')
  for j in range(i*2-1):
    if j == 0 or j == i*2-2:
      print("*", end='')
    else:
      print(" ", end='')
  
  print(end='\n')