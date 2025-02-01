#1912
from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(dp)
print(max(dp))





