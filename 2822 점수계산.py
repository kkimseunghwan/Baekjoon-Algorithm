from sys import stdin
score = []
for _ in range(8):
    score.append(int(stdin.readline().strip()))
maxscore = sorted(score, reverse=True)[:5]
print(sum(maxscore))

answer = []
for i in maxscore:
    answer.append(score.index(i)+1)
answer.sort()
print(' '.join(map(str, answer)))