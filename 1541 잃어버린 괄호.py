#1541 잃어버린 괄호
from sys import stdin

N = [sum(list(map(int, i.split("+")))) for i in list(stdin.readline().strip().split("-"))]
f = N[0]
for i in range(1, len(N)):
  f -= N[i]
print(f)