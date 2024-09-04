N, K = map(int, input().split()) # (1 ≤ K ≤ N ≤ 5,000)
p = list(range(1, N+1))

answer = []
nowIndex = 0
while p: # O(N) - O(5,000)
  nowIndex = nowIndex + (K-1)
  if nowIndex >= len(p):
    nowIndex = nowIndex % len(p)
  
  answer.append(p[nowIndex])
  del p[nowIndex]
  if nowIndex > len(p):
    nowIndex -= len(p)

print('<' + ', '.join([str(x) for x in answer]) + '>')