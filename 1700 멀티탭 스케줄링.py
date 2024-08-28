from sys import stdin
N, M = map(int, stdin.readline().split()) #  (1 ≤ N, M ≤ 100)
K = list(map(int, stdin.readline().split())) # 전기용품의 이름이 K 이하의 자연수 M개 O(M)
plugs = []
use = {} # 사용 횟수 저장.
for i in K: # K 만큼 반복. 최대 100번. O(M)
  if i in use: # 딕셔너리 내부 탐색. O(1)
    use[i] += 1
  else:
    use[i] = 1

cnt = 0
for p in range(M): # 각 리스트의 자리수 검사. O(M)
  nowPlug = K[p]

  if nowPlug in plugs: # 플러그가 꽃힌 상태라면 패스. 내부 검사 O(N)
    use[nowPlug] -= 1
    continue

  if len(plugs) < N: # 플러그가 비어있으면 추가. 플러그 내부 검사 O(N)
    plugs.append(nowPlug)
    use[nowPlug] -= 1
    continue

  # 1. 더 이상 사용되지 않는 애.
  # 2. 순서가 가장 나중에 있는 것
  lastPlug = -1
  unplug = 0
  for plug in plugs: # O(N)
    if use[plug] == 0:
      unplug = plug
      break
    else:
      if K[p+1:].index(plug) > lastPlug:
        lastPlug = K[p+1:].index(plug)
        unplug = plug
        
  
  plugs[plugs.index(unplug)] = nowPlug
  use[nowPlug] -= 1
  cnt += 1

print(cnt)


# 최종 시간 복잡도. O(M * N)
