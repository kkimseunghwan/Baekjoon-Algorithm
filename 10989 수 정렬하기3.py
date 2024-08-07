#10989 수 정렬하기3
from sys import stdin

def MergeSort(num):
  if len(num) <= 1:
    return num
  pivot = len(num)//2
  numLeft = num[:pivot]
  numRight = num[pivot:]
  L = MergeSort(numLeft)
  R = MergeSort(numRight)
  
  return Merge(L, R)

def Merge(L, R):
  result = []
  i = j = 0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      result.append(L[i])
      i += 1
    else:
      result.append(R[j])
      j += 1
  result += L[i:]
  result += R[j:]
  return result

N = int(stdin.readline())
num = []
cnt = {}
for i in range(N):
  l = int(stdin.readline())
  if l in cnt:
    cnt[l] += 1
  else:
    cnt[l] = 1
    num.append(l)

for i in MergeSort(num):
  for _ in range(cnt[i]):
    print(i)



