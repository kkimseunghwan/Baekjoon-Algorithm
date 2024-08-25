#9375 패션왕 신유빈
from sys import stdin

t = int(stdin.readline()) # 테스트 케이스 t 최대 100개 

for _ in range(t): # O(N)
  n = int(stdin.readline()) # 의상 수 n(0 ≤ n ≤ 30)
  wear = {}
  cnt = 1
  for _ in range(n): # 최대30 - 상수로 간주
    a, b = map(str, stdin.readline().split())
    if b in wear:   wear[b] += 1
    else:           wear[b] = 1

  wear = list(wear.values()) # 리스트 변환 최대30 - 상수로 간주
  
  for i in wear: # 최대30
    cnt *= i+1
  print(cnt-1)

# O(N)