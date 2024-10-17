#10798
from sys import stdin

messege = []
Max = 0
for _ in range(5):
	m = list(stdin.readline().strip())
	messege.append(m)
	Max = max(Max, len(m))

read = ""

for i in range(Max):
	for m in messege:
		if len(m) > i:
			read += m[i]

print(read)		
	

	