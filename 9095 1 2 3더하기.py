#9095 1 2 3더하기
from sys import stdin
tcase = int(stdin.readline())
for _ in range(tcase):
  N = int(stdin.readline())
  dp = [0] * (N+1)

  for i in range(N+1):
    if i < 2:
      dp[i] = 1
    elif i < 3:
      dp[i] = dp[i-1] + 1
    elif i < 4:
      dp[i] = dp[i-1] + dp[i-2] + 1
    else:
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  
  print(dp[-1])
