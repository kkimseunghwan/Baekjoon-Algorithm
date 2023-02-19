# X 강해져서 돌아와라 #

a = input()

order = 0
num = 1


while True:
  j = 2
  while num%(j**2) != 0:
    if num < (j**2):
      print("", num)
      order += 1
      break
    j += 1
    
  if order == int(a):
    print(num)
    break
  num += 1



