
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
num = [int(stdin.readline()) for _ in range(N)]
for i in MergeSort(num):
  print(i)
