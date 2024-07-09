from sys import stdin
N, M = map(int, stdin.readline().split())
site = {}
for _ in range(N):
  siteName, password = stdin.readline().split()
  site[siteName] = password

for _ in range(M):
  print(site[stdin.readline().strip()])



