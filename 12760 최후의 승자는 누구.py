 
from sys import stdin

N, M = map(int, stdin.readline().    split())

card = []
score = dict.fromkeys(range(1, N+1), 0)

for _ in range(N):
  card.append(sorted(list(map(int, stdin.readline().split())), reverse=True))

for i in range(M):
  maxScore = max([card[x][i] for x in range(N)])
  for j in range(N):
    if card[j][i] == maxScore:
      score[j+1] += 1


answer = [str(x+1) for x in range(N) if score[x+1] == max(score.values())]
print(' '.join(answer))
  