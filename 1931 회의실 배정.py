from sys import stdin
N = int(stdin.readline()) # (1 ≤ N ≤ 100,000)
workTime = []
for _ in range(N): # O(N) 최악 O(100,000)
  # 시작 시간과 끝나는 시간은 2^31 -1 (1,073,741,823)보다 작거나 같은 자연수 또는 0
  workTime.append(list(map(int, stdin.readline().split())))

# sort 함수는 Timsort 알고리즘을 사용. O(N LogN)
workTime.sort(key = lambda x: (x[0], x[1]))

# 최적 회의 시간 검사
lastTime, count_List = [], []
for x in workTime: # O(N) 최악 O(100,000)
  if lastTime == []:
    lastTime = x
  elif lastTime[1] <= x[0]:
    count_List.append(lastTime)
    lastTime = x
  elif ((x[1] - x[0]) < (lastTime[1]-lastTime[0])) and (lastTime[1] >= x[1]):
    lastTime = x
else:
  # 모든 루프 검사 후, 마지막 남은 시간 추가
  count_List.append(lastTime)

print(len(count_List)) # O(N) 최악 O(100,000)


# O(N+N+N+N+NLogN) -> O(NLogN)
  
