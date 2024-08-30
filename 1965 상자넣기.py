from sys import stdin

n = int(stdin.readline()) # n (1 ≤ n ≤ 1000)
box = list(map(int, stdin.readline().split())) # 각 입력값은 1,000을 넘지 않는 자연수
dp = [1] * n # O(n)

for i in range(1, n): # O(n)
  for j in range(i):# O(n)
    if box[j] < box[i]:
      dp[i] = max(dp[i], dp[j]+1)


print(max(dp))

# O(n^2)