from sys import stdin
import decimal
import math
def rounding(a):
  a = decimal.Decimal(a)
  if a % 1 >= 0.5:
      return int(math.ceil(a))
  else:
      return int(math.floor(a))
N = int(stdin.readline().strip())
if N == 0:
  print(0)
  exit()
numList = []
for _ in range(N):
  numList.append(int(stdin.readline().strip()))
nLen = len(numList)
k = rounding(decimal.Decimal(nLen * 0.15))
if k != 0 and k * 2 < nLen:
  numList.sort()
  del numList[:k]
  del numList[-k:]
print(int(rounding(decimal.Decimal(sum(numList)/(nLen - k*2)))))