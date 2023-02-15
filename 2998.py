def Make8Number(number):
  returnNum = ""
  while len(number) % 3 != 0:
      number = "0" + number
  
  for i in range(0, len(number), 3):
    plus = 0
    if int(number[i]) == 1:
      plus += 4
    if int(number[i+1]) == 1:
      plus += 2
    if int(number[i+2]) == 1:
      plus += 1
    returnNum += str(plus)

  return int(returnNum)

num = input()
print(Make8Number(num))
