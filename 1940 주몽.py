
#1940

from sys import stdin


N = int(stdin.readline()) # (1 ≤ N ≤ 15,000)
M = int(stdin.readline()) # (1 ≤ M ≤ 10,000,000) 
iron = sorted(list(map(int, stdin.readline().split())))

left, right = 0, N-1
answer = 0

while left < right:
	if iron[left] + iron[right] == M:
		answer += 1
		left += 1
		right -= 1
	elif iron[left] + iron[right] < M:
		left += 1
	elif iron[left] + iron[right] > M:
		right -= 1
		
print(answer)



