from sys import stdin
N, L, H = map(int, stdin.readline().split())
score = sorted(list(map(int, stdin.readline().split())))[L:N-H]
print(sum(score)/len(score))