a = int(input())

students = [ [*map(int, input().split())] for _ in range(a) ]  
studentsClass = []
for i in range(5):
  studentsClass.append([])
  for j in range(a):
    studentsClass[i].append(students[j][i])

asd = [0] * a

for i in studentsClass:
  for j in range(a):
    asd[j] += i.count(i[j])-1 


print(asd.index(max(asd))+1)

# *문제* 중복되었을 경우를 제외시켜야됨