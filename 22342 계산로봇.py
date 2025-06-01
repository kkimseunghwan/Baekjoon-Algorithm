from sys import stdin

# (행 번호, 열 번호) => (y, x)
M, N = map(int, stdin.readline().split())

# 각각의 줄은 한 행에 해당하며 N개의 숫자(한 자리 수)로 이루어진 문자열이 주어진다.
D = []
for _ in range(M):
    D.append([int(i) for i in stdin.readline().strip()])

# 각 로봇은 하나 이상의 입력 값, 하나의 저장 값, 하나의 출력 값을 가진다.
#       제일 왼쪽 열에 있는 로봇의 입력 값은 0 하나로 정한다
#       제일 왼쪽 열에 있는 로봇의 출력값 => 0 + 가중치
#       입력 값들 중 최댓값을 자신의 저장 값
#       (저장 값, 출력 값)
robots = [[[0, 0] for _ in range(N)] for _ in range(M)]

for i in range(M):
    robots[i][0][1] += D[i][0]


# 좌표 (i, j)의 로봇의 입력 값은 |i−a| ≤ j −b, b < j인 모든 좌표 (a, b)
# 에 있는 로봇들의 출력 값들이다.
# 중 최댓값을 자신의 저장 값
def getInputXY(y, x, M=M, N=N, robots=robots):
    max_output = 0
    miny = 0 if y == 0 else y - 1
    maxy = M-1 if y == M-1 else y + 1

    for a in range(miny, maxy+1):
        if max_output < robots[a][(x-1)][1]:
            max_output = robots[a][(x-1)][1]

    return max_output

max_save = 0
        
for x in range(1, N):
    for y in range(M):
        robots[y][x][0] = getInputXY(y, x)
        if max_save < robots[y][x][0]:
            max_save = robots[y][x][0]
        robots[y][x][1] = robots[y][x][0] + D[y][x]

print(max_save)

