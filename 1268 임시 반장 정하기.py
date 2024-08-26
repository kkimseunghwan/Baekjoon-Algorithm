#1268 임시 반장 정하기
from sys import stdin
students = int(stdin.readline()) # 학생 수 3 이상 1000 이하
student_dict = dict.fromkeys(list(range(1, students+1)), 0)

classes = []
for _ in range(students): # 최대 100번 반복 O(N)
  # 1학년 ~ 5학년 반 입력. 입력 개수 5개 고정.
  classes.append(list(map(int, stdin.readline().split()))) # 주지는 정수는 모두 1 이상 9 이하의 값

# 각 학생의 반 검사. 마지막은 제외. 
# 왜 WHY? 순차적으로 검사하면, 마지막 애는 자기 자신외에 다른 애들 모두와 검사를 한 상태일 것이기 때문에.
for i in range(len(classes)-1): # 최대 999번 반복. O(N)
  for j in range(i+1, len(classes)): # 상위 반복문에 따라 루프 횟수가 줄어듬 O(N/2) -> O(N)
    for n in range(5): # 학년은 총 5학년. 상수값5. O(1)
      if classes[i][n] == classes[j][n]:
        student_dict[i+1] += 1
        student_dict[j+1] += 1
        break
     
# 최대값 찾기.
answer, max = 0, -1
for key, value in student_dict.items():
  if value > max:
    max = value
    answer = key
    
print(answer)

# 최종 시간 복잡도 O(N^2)



