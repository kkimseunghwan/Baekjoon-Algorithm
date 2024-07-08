from sys import stdin
N = 1000 - int(stdin.readline())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in money:
  if (N % i) != N:
    cnt += N//i
    N -= (N//i) * i
  if i == 0: break
    
print(cnt)