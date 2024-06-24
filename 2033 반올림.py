from sys import stdin
n = int(stdin.readline().strip())
i = 1
while True : 
  if 10**i <= n:
    n = round(n+1, -i) if int(str(n)[-i]) >= 5 else round(n, -i)
  else:
    break
  i += 1
print(n)