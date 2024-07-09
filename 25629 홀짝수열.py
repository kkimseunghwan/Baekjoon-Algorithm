from sys import stdin
N = int(stdin.readline().strip())
numList = list(map(int, stdin.readline().split()))
hl,jl = N//2 if N%2 == 0 else N//2+1,N//2
h,j=[], []
answer = 0
for i in numList:
  if (i % 2) != 0:
    h.append(i)
  else:
    j.append(i)
if hl == len(h) and jl == len(j):
  answer = 1
print(answer)
