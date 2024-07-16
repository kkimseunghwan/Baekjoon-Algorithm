from sys import stdin

tcase = int(stdin.readline())
strAll = ""
while tcase:
  N = stdin.readline().strip()
  strAll += N
  if N == "":
    print("Efficiency ratio is %g%%." %(round(100 - strAll.count('#')/len(strAll) * 100, 1)))
    strAll = ""
    tcase -= 1
    continue