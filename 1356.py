import math

a = list(input())
if len(a) > 1:
  for i in range(len(a)):
    a[i] = int(a[i])

  for i in range(len(a)):
    if math.prod(a[:i]) == math.prod(a[i:]):
      #print(a)
      print("YES")
      exit()

print("NO")