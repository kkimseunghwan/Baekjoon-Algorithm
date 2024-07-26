#11659 구간 합 구하기3
from sys import stdin

N, M = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))
sum = [0] * (N)
ln = 0
for i in range(N):
  ln = ln + num[i] if i > 0 else num[i]
  sum[i] = ln

for _ in range(M):
  a, b = map(int, stdin.readline().split())  
  print(sum[b-1] - sum[a-2] if a > 1 else sum[b-1])
