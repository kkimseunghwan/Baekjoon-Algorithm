#5179 우승자는누구
from sys import stdin
tcase = int(stdin.readline())
for q in range(tcase):
  #M 문제의 개수, N은 총 제출 수, P 참가자의 수.
  M, N, P = map(int, stdin.readline().split())
  test = []
  for _ in range(N):
    p, m, t, j = map(str, stdin.readline().split())
    test.append([int(p), m, int(t), int(j)])
    test = sorted(test, key = lambda x : (x[0], x[1], x[2]))
    
  answer = [[i, 0, 0] for i in range(1, P+1)]
  wrong, nowMode, isRight = 0, '', False
  nowPlayer = 0
  for i in test:
    if i[0] != nowPlayer:
      isRight = False
      wrong = 0
      nowMode = i[1]
      nowPlayer = i[0]
    elif i[1] != nowMode:
      wrong = 0
      isRight = False
      nowMode = i[1]
      
    if i[3] == 1 and not isRight:
      isRight = True
      answer[i[0]-1][1] += 1
      answer[i[0]-1][2] += i[2] + wrong*20
    elif i[3] == 0:
      wrong += 1
  print("Data Set {:d}:".format(q+1))
  for i in sorted(answer, key = lambda x : (-x[1], x[2])):
    print(' '.join(list(map(str, i))))
  print()