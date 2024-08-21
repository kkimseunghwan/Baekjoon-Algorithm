#10431 줄세우기
from sys import stdin
N = int(stdin.readline()) # P (1 ≤ P ≤ 1000)

# 테스트 케이스에 따라 아래 작업 반복 O(N) 
for _ in range(N):
  # 테스트 케이스 번호 T와 20개의 양의 정수가 공백으로 구분되어 주어진다.
  # 입력되는 정수 배열 크기는 20개로 고정됨으로 O(1)
  num = list(map(int, stdin.readline().split()))
  students = num[1:]

  jump = 0
  line = [students.pop(0)] # pop(0)은 O(1)

  # 반복문 최악의 경우 19번 반복
  for i in students:
    line.append(i) # append는 O(1)
    for l in range(len(line)-1): # 반복문 최악의 경우 19번 반복
      if line[l] > i: # 조건 만족하여 작업 최악의 경우 O(19)
        backLine = line[l:-1]
        line[l] = i
        line[l+1:] = backLine
        jump += len(line)-l-1 # 단순 계산 O(1)
        break

  print(num[0], jump)
  

# 최종 시간복잡도 O(N)
