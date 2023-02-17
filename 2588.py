a = int(input())
b = int(input())

for i in range(2, -1, -1):
  print(a * int(str(b)[i]))
print(a*b)