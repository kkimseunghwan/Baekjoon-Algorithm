from sys import stdin
N, M = map(int, stdin.readline().split())
money = []
for _ in range(N):
  money.append(int(stdin.readline().strip()))
cnt = 0
money = sorted(money, reverse = True)
for i in money:
  if M == 0: break
  if (M % i) != M:
    cnt += M // i
    M = M % i
print(cnt)
    