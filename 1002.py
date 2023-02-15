import math

num = int(input())

answer = 0
for i in range(0, num):
  zoX, zoY, zoR, baX, baY, baR = map(int, input().split())

  for j in range(0, 360, 15):
    #print(f"{j:2d}\t{math.sin(math.radians(j)):.4f}\t{math.cos(math.radians(j)):.4f}")
    if (zoX + (zoR * math.cos(math.radians(j)))) == (baX + (baR * math.cos(math.radians(j)))):
      if (zoY + (zoR * math.sin(math.radians(j)))) == (baY + (baR * math.sin(math.radians(j)))):
        answer += 1
  print(answer)
      
#############  No ###############Q











