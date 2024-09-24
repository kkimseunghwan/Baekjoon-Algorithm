
#1806

from sys import stdin

# N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)
N, S = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

start, end = 0, 0

nowSum = nums[0]
min_len = 0
while end < N and start < N:
	if nowSum >= S:
		min_len = (end+1) - start if min_len == 0 else min(min_len, (end+1) - start)		
		nowSum -= nums[start]
		start += 1
	elif end < N -1:
		end += 1
		nowSum += nums[end]
	else:
		break

print( min_len )
