from sys import stdin
N = int(stdin.readline().strip())
time = sorted(list(map(int, stdin.readline().split())))
nowTime = 0
for i in range(len(time)):
    nowTime += sum(time[:i+1])
print(nowTime)