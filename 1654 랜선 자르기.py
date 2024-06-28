from sys import stdin

def testing(list, N):
  plus = 0
  for i in list:
    plus += (i // N)
  return plus

K, T = map(int, stdin.readline().split())
ln = []
for _ in range(K):
  ln.append(int( stdin.readline().strip()))

lanMin = 1
lanMax = max(ln)
result = 0
while lanMin <= lanMax:
  pivot = (lanMin + lanMax) // 2
  if testing(ln, pivot) >= T:
    result = pivot
    lanMin = pivot + 1
  else:
    lanMax = pivot - 1
print(result)