
from sys import stdin

#랭킹 리스트에 있는 점수 N개 ( 0 <= N <= P )
#태수의 새로운 점수 S
#랭킹 리스트에 올라 갈 수 있는 점수의 개수 P ( 10 <= P  <= 50 )
N, S, P = map(int, stdin.readline().split())
rank = []
ranking = list(range(1, P+1))

if N <= 0:
	print(1)
	exit()

rank = list(map(int, stdin.readline().split()))

if N >= P and rank[-1] >= S:
	print(-1)
	exit()

rank.append(S)
rank = sorted(rank, reverse = True)

for i in range( 1, min(N+1, P) ):
	if rank[i] == rank[i-1]:
		ranking[i] = ranking[i-1]
		
print(ranking[rank.index(S)])

