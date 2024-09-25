#5525
from sys import stdin

N = int(stdin.readline()) # 1 ≤ N ≤ 1,000,000
M = int(stdin.readline()) # 2N+1 ≤ M ≤ 1,000,000

P = 'I' + ('OI' * N)
P_len = 1 + N*2

S = stdin.readline().strip()

pattern_cnt, start, cnt = 0, 0, 0

while start < (M - 3):
	if S[start : start+3] == "IOI":
		start += 2
		pattern_cnt += 1
		
		if pattern_cnt == N:
			cnt += 1
			pattern_cnt -= 1
	else:
		start += 1
		pattern_cnt = 0

print(cnt)


