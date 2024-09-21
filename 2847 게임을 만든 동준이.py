
from sys import stdin

N = int(stdin.readline()) # N (1 ≤ N ≤ 100) 
score = []
for _ in range(N): # O(N) -> O(100)
    score.append(int(stdin.readline()))

answer = 0
for i in range(N-1): # O(N) -> O(100)
    if score[i] > score[-1]-(N-1-i):
        nowScore = score[i]
        changeScore = score[-1]-(N-1-i)
        answer += nowScore - changeScore
        score[i] = changeScore


while True: # O(N) -> O(10000)
    for i in range(N-1): 
        if score[i] >= score[i+1]:
            nowScore = score[i]
            changeScore = score[i+1] - 1
            answer += nowScore - changeScore
            score[i] = changeScore
            break
    else:
        break


print(answer)
