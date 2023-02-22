
while True:
  a = input()
  if a == "0": break
  space = 1
  for i in a:
    space += 1
    if i == "0": space += 4
    elif i == "1": space += 2
    else: space += 3
  print(space)