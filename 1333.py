
N, L, D = map(int, input().split())

val = 1
while True:
  time = L + 5
  d = D * val
  for i in range(1, N+1):
    time = time * i
    if time-5 <= d and time > d:
      print(d)
      exit()
    time = L + 5

  val += 1
  
  if d >= time * N:
    print(d)
    break

