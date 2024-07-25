#2579 계단오르기
from sys import stdin
N = int(stdin.readline())
stairs = [0] + [int(stdin.readline()) for _ in range(N)]
dp = [0] * (N+1)
for i in range(1, N+1):
  if i < 2:
    dp[i] = stairs[i]
  elif i < 3: 
    dp[i] = dp[i-1] + stairs[i] 
    
  elif  dp[i-1] != dp[i-4] + stairs[i-2] + stairs[i-1]:
    dp[i] = max(dp[i-1], dp[i-2]) + stairs[i]
  else:
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[-1])