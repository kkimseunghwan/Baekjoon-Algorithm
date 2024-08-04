from sys import stdin
import re

N = int(stdin.readline())
guitar = [stdin.readline().strip() for _ in range(N)]

for i in sorted(guitar, key = lambda x : ( len(x), sum(list(map(int, re.findall(r'\d', x)))), x):
  print(i)

