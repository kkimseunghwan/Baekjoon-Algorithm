
from sys import stdin

def ApartCount(grid, N):
  answer = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 1:
        cnt = DFS(grid, N, i, j)
        answer.append(cnt)

  return len(answer), answer

def DFS(grid, N, y, x):
  connect = [ (1, 0), (0, 1), (-1, 0), (0, -1) ] 
  stack = [ (y, x) ]
  grid[y][x] = 0
  apart_cnt = 1

  while stack:
    i, j = stack.pop()
    for nx, ny in connect:
      x = j + nx
      y = i + ny
      if (0 <= x < N and 0 <= y < N) and grid[y][x] == 1:
        stack.append( (y, x) )
        grid[y][x] = 0
        apart_cnt += 1

  return apart_cnt

# N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25) 
N = int( stdin.readline() ) 

grid = []
for _ in range(N):
  apart = [ int(x) for x in stdin.readline().strip() ]
  grid.append(apart)


answer = ApartCount(grid, N)
print(answer[0])
for i in sorted(answer[1]):
  print(i)

'''
7
0110100
0110101
1111101
0000111
0100000
0111110
0111000


'''







