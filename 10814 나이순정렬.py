from sys import stdin
N = int(stdin.readline().strip())
ageData = []
for i in range(N):
  age, name = stdin.readline().strip().split()
  ageData.append([i+1, age, name])
ageData.sort(key = lambda x: (int(x[1]), x[0]))
for i in ageData:
  print(i[1], i[2])