from sys import stdin

# 3x3 행렬 뒤집기. 시작 좌표 (x, y)
def reverseArr(arr, x, y):
    if (len(arr) < y+3) or (len(arr[0]) < x+3):
        return False

    for i in range(3):
        for j in range(3):
            arr[y+i][x+j] = int(not arr[y+i][x+j])
    
    return True

N, M = map(int, stdin.readline().split())

arrA, arrB = [], []
for _ in range(N):
    arrA.append(list(map(int, stdin.readline().strip())))
for _ in range(N):
    arrB.append(list(map(int, stdin.readline().strip())))

if (N < 3 or M < 3) and (arrA != arrB):
    print(-1)
    exit()

answer = 0
for i in range(N):
    for j in range(M):
        if arrA[i][j] != arrB[i][j]:
            if reverseArr(arrA, j, i):
                answer += 1
if arrA == arrB:
    print(answer)
else:
    print(-1)



