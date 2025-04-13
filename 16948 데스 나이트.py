
'''
게임을 좋아하는 큐브러버는 
체스에서 사용할 새로운 말 
"데스 나이트"를 만들었다. 

데스 나이트가 있는 곳이 (r, c)라면, 
(r-2, c-1), 
(r-2, c+1), 
(r, c-2), 
(r, c+2), 
(r+2, c-1), 
(r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 
두 칸 (r1, c1), (r2, c2)가 주어진다. 

데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 
최소 이동 횟수를 구해보자. 
체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)
둘째 줄에 r1, c1, r2, c2

>> 첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 
최소 이동 횟수를 출력한다. 
이동할 수 없는 경우에는 -1을 출력한다.
'''

from sys import stdin
from collections import deque

knightMove = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
def BFS(N, r1, c1, r2, c2):
    chessFeild = list()
    for _ in range(N):
        chessFeild.append([0]*N)

    chessFeild[r1][c1] = 1
    
    start, target = (r1, c1), (r2, c2)
    
    queue = deque()
    queue.append(start)

    moveCnt = 0
    while queue:
        moveCnt += 1
        for _ in range(len(queue)):
            r_loc, c_loc = queue.popleft()
            for x, y in knightMove:
                if r_loc+x >= 0 and abs(r_loc+x) <= N-1 and c_loc+y >= 0 and abs(c_loc+y) <= N-1:
                    if (r_loc+x, c_loc+y) == target:
                        return moveCnt
                    elif chessFeild[r_loc+x][c_loc+y] == 0:
                        chessFeild[r_loc+x][c_loc+y] = 1
                        queue.append((r_loc+x, c_loc+y))

        

    return -1

# 체스판의 크기 N(5 ≤ N ≤ 200)
N = int(stdin.readline())

# (r1, c1)에서 (r2, c2)로 이동
r1, c1, r2, c2 = map(int, stdin.readline().split())

print(BFS(N, r1, c1, r2, c2))

