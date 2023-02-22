import sys

def PlusOrMinus(max):
    if max == 0:
      return 0
    elif max > 0:
      return "+"
    elif max < 0:
      return "-"

for j in range(3):
  max = 0
  for i in range(int(input())):
    max += int(sys.stdin.readline().rstrip())
  print(PlusOrMinus(max))

