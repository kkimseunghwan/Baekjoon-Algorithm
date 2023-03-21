case = input()
num = [*map(int, input().split())]

print(num)

loop = len(num)
index = 0
while True:
  if index == len(num)-1:
    if loop == len(num):
      break
    else:
      loop = len(num)
      index = 0
  if num[index] >= num[index+1]:
    del num[index]
    print(num)
    continue
  index += 1

print(len(num))
