#9461 파도반 수열
from sys import stdin

tcase = int(stdin.readline())
for _ in range(tcase):
  N = int(stdin.readline())
  dp = [1] * N
  for i in range(N):
    if i > 2:
      dp[i] = dp[i-2] + dp[i-3]
  print(dp[-1])