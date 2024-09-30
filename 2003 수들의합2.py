
#2003
from sys import stdin
# N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
N, M = map(int, stdin.readline().split())

Arr = list(map(int, stdin.readline().split()))
start, end = 0, 0
nowSum = Arr[0]
cnt = 0

while start < N and end < N:
	if nowSum < M:
		end += 1
		if end < N: nowSum += Arr[end]
	elif nowSum >= M:
		if nowSum == M:
			cnt += 1
		nowSum -= Arr[start]
		start += 1

print(cnt)
