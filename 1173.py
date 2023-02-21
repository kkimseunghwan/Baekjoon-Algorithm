N, m, M, T, R = map(int, input().split())

X = m
time = 0
ex = 0
while True:
  if X+T <= M: #운동 후 최대 맥박을 넘지 않을 때
    X = X+T
    ex += 1
  elif X+T > M: #맥박으로 인해 운동을 못할 때
    if X-R < m: X = m
    else: X = X-R
  if m+T > M:
    print(-1)
    break
  time += 1
  if ex == N: 
    print(time)
    break


