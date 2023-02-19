arr = []
max = 0
for i in range(0, 9):
  a = int(input())
  arr.append(a)
  if max <= a: max = a

print(max)
print(arr.index(max)+1)