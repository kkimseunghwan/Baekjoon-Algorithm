from sys import stdin
numList = list(map(int, stdin.readline().split()))
numList.extend(reversed(list(map(int, stdin.readline().split()))))
m, answer = 0, 0
for i in range(4):
  result = (numList[0]/numList[2] + numList[1]/numList[3])
  if m < result:
    m = result
    answer = i
  numList.extend(numList[:3])
  del numList[:3]
print(answer)