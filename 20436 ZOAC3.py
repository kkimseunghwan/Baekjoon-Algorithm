from sys import stdin

left = 'qwertasdfgzxcv_' # 15
right = '_yuiop_hjkl_bnm___' # 18

start_L, start_R = map(str, stdin.readline().split())
txt = stdin.readline().strip()  # 문자열의 길이는 최대 100자

cnt = 0
for i in txt: # 최대 O(100)
  x, y, nx, ny = -1, -1, -1, -1
  if i in left: # O(15)
    x = left.index(i) % 5 # O(15)
    y = left.index(i) // 5 # O(15)

    nx = left.index(start_L) % 5 # O(15)
    ny = left.index(start_L) // 5 # O(15)

    start_L = i
  else:
    x = right.index(i) % 6 # O(18)
    y = right.index(i) // 6 # O(18)

    nx = right.index(start_R) % 6 # O(18)
    ny = right.index(start_R) // 6 # O(18)

    start_R = i

  cnt += 1 + abs(x - nx) + abs(y - ny)

print(cnt)
# O(N)