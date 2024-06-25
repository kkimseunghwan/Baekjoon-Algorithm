from sys import stdin
N = stdin.readline()
num1 = set(map(int, stdin.readline().split()))
N = stdin.readline()
num2 = list(map(int, stdin.readline().split()))

for i in num2:
  if i in num1:
    print(1)
  else:
    print(0)