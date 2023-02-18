num = input()

if int(num) < 0 or int(num) > 99: exit()

if len(num) == 1: num = "0" + num
firstNum = num

count = 0
while True:
  count += 1
  num = num[-1] + str(int(num[0]) + int(num[1]))[-1]
  if num == firstNum: break

print(count)
