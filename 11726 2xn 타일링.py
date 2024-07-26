#11726 2xn 타일링
from sys import stdin
N = int(stdin.readline())
dp = [0] * (N+1)
for i in range(1, N+1):
  if i < 2:
    dp[1] = 1
  elif i < 3:
    dp[2] = 2
  else:
    dp[i] = dp[i-1] + dp[i-2]
print(dp[-1]%10007)