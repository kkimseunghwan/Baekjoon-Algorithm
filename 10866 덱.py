
#10866 덱
from collections import deque
from sys import stdin

N = int(stdin.readline()) # N (1 ≤ N ≤ 10,000)
queue = deque([])

for _ in range(N):
  debug = stdin.readline().strip().split(' ')
  if   debug[0] == 'size': print(len(queue))
  elif debug[0] == 'empty': print( 1 if not queue else 0)
  elif debug[0] == 'front': print( queue[0] if queue else -1)
  elif debug[0] == 'back': print( queue[-1] if queue else -1)
  elif debug[0] == 'push_front': queue.appendleft(debug[1])
  elif debug[0] == 'push_back': queue.append(debug[1])
  elif debug[0] == 'pop_front': print( queue.popleft() if queue else -1)
  elif debug[0] == 'pop_back': print( queue.pop() if queue else -1)
