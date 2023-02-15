def Make8Number(number):
  strNum = str(number)
  returnNum = ""
  while True:
    if len(strNum) % 3 != 0:
      strNum = "0" + strNum
    else: break
  
  for i in range(0, len(strNum), 3):
    plus = 0
    if int(strNum[i]) == 1:
      plus += 4
    if int(strNum[i+1]) == 1:
      plus += 2
    if int(strNum[i+2]) == 1:
      plus += 1
    returnNum += str(plus)

  return int(returnNum)

num = int(input())
print(Make8Number(num))
