#27674
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
	null = stdin.readline().strip()
	num = sorted(list(stdin.readline().strip()), key = lambda x: -int(x) )
	a = int(''.join(num[:-1]))
	b = int(num[-1])
	print(a+b)
	
	
	