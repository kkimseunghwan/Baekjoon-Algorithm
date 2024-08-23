#2941 크로아티아 알파벳
from sys import stdin
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
txt = stdin.readline().strip() # 최대 100글자
answer = len(txt)

for i in croatia: # 8번 반복. O(8)
  if i in txt: # O(N)
    cnt = txt.count(i) # O(N)
    answer -= (1 if i != 'dz=' else 2) * cnt 
    txt = txt.replace(i, ' ') # O(N)

print(answer)

# 시간복잡도 O(8) * ( O(N) + O(N) + O(N) ) = O(24N) = 상수제거 = O(N)

