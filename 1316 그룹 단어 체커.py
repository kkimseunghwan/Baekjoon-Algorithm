#1316 그룹 단어 체커
from sys import stdin
N = int(stdin.readline()) # N은 100보다 작거나 같은 자연수이다 (0도 되나?)
answer = 0 # 결과를 저장 할 변수 

for _ in range(N): # O(N) 최악의 경우 100번 반복 
  txt = stdin.readline().strip() #입력 길이는 L로 최대 100이다.
  group = [] # 그룹 단어를 저장하는 리스트
  for i in range(len(txt)): # O(L) 최악의 경우 100번 반복 => 루프 및 탐색 시간복잡도 O(L^2)
    if not group: # 그룹 내부가 비어있을 때.
      group.append(txt[i])
    else:
      if txt[i] not in group: # O(L) 문자열 길이에 따라 반복. 최악의 경우 100번 반복
        group.append(txt[i])
      elif txt[i] != group[-1]:
        break
  else:
    answer += 1

print(answer)

# 최종 시간복잡도 O(N * L^2) 
# 최악의 경우 O(100^3)




