# 2559

from sys import stdin

N, K = map(int, stdin.readline().split())

temp = list(map(int, stdin.readline().split()))

nowTemp = sum(temp[0:K])
maxTemp = nowTemp

for i in range( 1, N - K + 1 ):
	nowTemp = nowTemp - temp[i - 1] + temp[i + K - 1]
	if nowTemp >  maxTemp:
		maxTemp = nowTemp
		
print(maxTemp)

