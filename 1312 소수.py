 
from sys import stdin

A, B, N = map(int, stdin.readline().split())

remain = A % B
for i in range(N):
  remain *= 10
  if i == N - 1:
    print(remain // B)
  else:
    remain %= B


