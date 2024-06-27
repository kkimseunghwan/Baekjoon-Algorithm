from sys import stdin

while True:
  N = stdin.readline().split('.')[0]
  if len(N) == 0:
    break
  strList = []
  for i in N:
    if i in ("(", "["):
      strList.append(i)
    elif i in (")" ,"]"):
      if len(strList) > 0: 
        pp = strList.pop()
      else:
        print("no")
        break
      if not (pp == "(" and i == ")") and not (pp == "[" and i == "]"):
        print("no")
        break
  else:
    if len(strList) == 0:
      print("yes")
    else:
      print("no")
