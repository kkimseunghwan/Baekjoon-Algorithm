
textDict = {}
try:
  while True: # O(L)
    line = input() # 각 줄은 최대 50개의 글자로 이루어져 있다. 
    for i in line: # O(N) 최대 50개
      if i == ' ': continue
      if i in textDict:
        textDict[i] += 1
      else:
        textDict[i] = 1
except EOFError:
  max_value = max(textDict.values())
  max_keys = [key for key, value in textDict.items() if value == max_value]
  max_keys.sort() # O(N LogN)
  print(''.join(max_keys))
  exit()

# O(N LogN)