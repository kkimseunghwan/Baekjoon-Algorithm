case = int(input())
arr = []

for i in range(case):
  arr.append(input())

search = arr[0]

if len(arr) > 1:
  for i in range(1, len(arr)):
    for j in range(0, len(search)):
      if arr[i][j] != search[j]:
        
        #list를 통해 특정 인덱스에서의 문자열의 문자 바꾸기 
        tmp = list(search)
        tmp[j] = '?'
        search = "".join(tmp)


print(search)
