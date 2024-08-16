from sys import stdin
N = stdin.readline()
gaji = list(map(str, stdin.readline().split()))
m, k = map(int, stdin.readline().split())
answer = 'P'
for _ in range(m):
  pl = list(map(int, stdin.readline().split()))
  tt = 'W'
  for i in pl:
    if gaji[i-1] == 'P':
      tt = 'P'
  if tt == 'W': 
    answer = 'W'

print(answer)
