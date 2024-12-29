
from sys import stdin

#자릿수 입력 받기
N = int(stdin.readline())

#각 자리수일때의 이친수의 개수 저장.
dp = [1] * N

#dp 관의 관계 : dp[i] = dp[i-1] + dp[i-2]
for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

# N자릿수의 이친수 출력
print(dp[-1])


## (+) 메모리 최적화 가능
# 이전 두 값을 이용해 계산
prev1, prev2 = 1, 1  # dp[0], dp[1]
for _ in range(2, N):
    current = prev1 + prev2
    prev1, prev2 = prev2, current

# N자리 이친수 개수 출력
print(prev2)



