
# 18258 큐2
from collections import deque
from sys import stdin

def push(X):
  queue.append(X)

def pop():
  print(queue.popleft() if queue else -1)

def size():
  print(len(queue))

def empty():
  print(1 if not queue else 0)

def front():
  print(queue[0] if queue else -1)

def back():
  print(queue[-1] if queue else -1)

commands = {
    'push':push,
    'pop':pop,
    'size':size,
    'empty':empty,
    'front':front,
    'back':back
}

queue = deque([])
N = int(stdin.readline()) # N (1 ≤ N ≤ 10,000)

for _ in range(N):
  command = stdin.readline().strip().split(' ')
  if command[0] != 'push':
    commands[command[0]]()
  else:
    commands[command[0]](command[1])

