#19532 수학은 비대칭
from sys import stdin 

x1, y1, z1, x2, y2, z2 = map(int, stdin.readline().split())
print((z2*y1-z1*y2) // (x2*y1-x1*y2), (z2*x1-z1*x2) // (y2*x1-y1*x2))
