from sys import stdin
mario = [int(stdin.readline().strip()) for _ in range(10)]
nowScore = 0
for i in range(len(mario)):
  if nowScore + mario[i] < 100:
    nowScore += mario[i]
  else:
    if abs(100 - nowScore) >= abs(100 - (nowScore + mario[i])):
      nowScore = nowScore + mario[i]
    break
print(nowScore)