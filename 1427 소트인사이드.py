#
from sys import stdin 
N = stdin.readline().strip()
print(''.join(reversed(sorted(list(N)))))

