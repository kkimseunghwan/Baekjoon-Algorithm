# 7785

from sys import stdin

# (2 ≤ n ≤ 10^6)  - (100만)  
n = int(stdin.readline())

enter = []
sysLog = {}

for _ in range(n):
	name, log = map(str, stdin.readline().split())
	if log == "enter":
		sysLog[name] = 1
	elif log == "leave":
		sysLog[name] = 0

for a, b in sysLog.items():
	if b == 1:
		enter.append(a)
		
print("\n".join(sorted(enter, reverse=True)))

