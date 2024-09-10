#  2960 에라토스테네스의 체

from sys import stdin

N, K = map(int, stdin.readline().split()) # (1 ≤ K < N  ≤ 1000)

num = list(range(2, N+1))

P = 0
while num:
	for i in range(len(num)):
		if i == 0: P = num[0]
		if num[i]%P == 0:
			K -= 1
			if K == 0:
				print(num[i])
				exit()
			num[i] = -1
	num = [ x for x in num if x != -1 ]
	
	