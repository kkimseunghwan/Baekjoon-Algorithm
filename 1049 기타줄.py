
# 1049
from sys import stdin

# N <= 100, M <= 50
N, M = map(int, stdin.readline().split())

DLC = 1000
One = 1000

for _ in range(M):
	priceDLC, priceOne = map(int, stdin.readline().split())
	DLC = min(DLC, priceDLC)
	One = min(One, priceOne)

price = 0

if N >= 6:
	if DLC < One * 6: price += DLC * (N//6)
	else: price += One * 6 * (N//6)
	N -= 6 * (N//6)

if N > 0:
	if DLC < One * N: price += DLC
	else: price += One * N


print(price)
	
	
