from sys import stdin

def fibonacci(n):
  a=[1,1]
  if n == 0:
    print(1, 0)
    return 0
  elif n == 1:
    print(0, 1)
    return 1
  for i in range(2, n):
    a.append(a[i-2] + a[i-1])
  print(a[-2], a[-1])


N = int( stdin.readline().strip())
for _ in range(N):
  fibonacci(int(stdin.readline().strip()))
