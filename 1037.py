
case = int(input())

arr = [*map(int, input().split())]
max = 0
min = 1000000
for i in arr:
  if max <= i: max = i
  if min >= i: min = i

print(max*min)



