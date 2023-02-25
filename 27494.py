serial = ["2", "0", "2", "3"]
a = int(input())
win = 0
arr = []
for i in range(2023, a+1):
  ind = 0
  arrIndex = [0, 0, 0, 0]
  if str(i).find("2") > 1 and "0" in str(i) and "3" in str(i):
    arr.append(i)

print(arr)
for i in arr:
  for j in range(len(serial)):
    #print(str(i)[ind:].find(serial[j]))
    if str(i)[ind:].find(serial[j]) != -1:
      arrIndex[j] = str(i)[ind:].find(serial[j])
      ind = str(i)[ind:].find(serial[j])
    
  if arrIndex[0] <= arrIndex[1] and arrIndex[1] <= arrIndex[2] and arrIndex[2] <= arrIndex[3]:
    print(i)
    win += 1
  
print(win)

