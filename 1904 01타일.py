from sys import stdin
N = int(stdin.readline())
num1, num2 = 1, 2

if N >= 2:
  for _ in range(2,N):
    num1, num2 = num2, (num1 + num2)%15746
else:
  num2 = 1

print(num2)
