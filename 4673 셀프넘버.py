#4673 셀프넘버
from sys import stdin
num = dict.fromkeys(list(range(1,10001)), 0) 
for a,b in num.items(): 
  D = a + sum(int(i) for i in str(a))
  if D <= 10000:
    num[D] = 1
  if b == 0:
    print(a)

# O(N + N) > O(2N) > O(N)