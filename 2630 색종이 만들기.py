#2630 색종이 만들기
import sys

N = int(sys.stdin.readline())
s = []
for _ in range(N):
  s.append(list(map(int, sys.stdin.readline().split())))

def check(squre, A, B, N):
  white, blue, sumLn = 0, 0, 0
  ln = []
  #전체 이중 배열에서 설정한 사각형의 범위만큼 배열로 생성
  for i in squre:
    ln.append(i[A:B])
    sumLn += sum(i[A:B])

  #DEBUG
  #print("SQURE")
  #for i in ln:
  #  print(i)

  if sumLn != 0 and sumLn != (N * N):
    i1, j1 = check(ln[:N//2], 0, N//2, N//2)
    i2, j2 = check(ln[:N//2], N//2, N, N//2)
    i3, j3 = check(ln[N//2:], 0, N//2, N//2)
    i4, j4 = check(ln[N//2:], N//2, N, N//2)

    white += i1 + i2 + i3 + i4
    blue += j1 + j2 + j3 + j4

  elif sumLn == 0:
    white += 1
  elif sumLn == (N * N):
    blue += 1

  return white, blue

for i in check(s, 0, N, N):
  print(i)
