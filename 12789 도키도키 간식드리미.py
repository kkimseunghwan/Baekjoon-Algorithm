from sys import stdin

N = int(stdin.readline())
line = list(map(int, stdin.readline().split()))
stack = []
nowNum = 1

while line or stack:   
  if stack and stack[-1] == nowNum:
    stack.pop()
    nowNum += 1
  elif N > 0:
    if line[0] == nowNum:
      nowNum += 1
    else:
      stack.append(line[0])
    del line[0]
    N -= 1
  else:
    print("Sad")
    break
else:
  print("Nice")
