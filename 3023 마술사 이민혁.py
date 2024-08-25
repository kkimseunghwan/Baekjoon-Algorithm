
from sys import stdin
R, C = map(int, stdin.readline().split())

card = []
for _ in range(R):
  pattern = stdin.readline().strip()
  pattern += pattern[::-1]
  card.append(list(pattern))
for i in range(len(card)-1,-1,-1):
  card.append(card[i][:])

A, B = map(int, stdin.readline().split())
card[A-1][B-1] = '.' if card[A-1][B-1] == '#' else '#'

for i in card:
  print(''.join(i))





