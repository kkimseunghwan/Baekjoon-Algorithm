N = int(input())
F = int(input())

arr = str(N)
tmp = list(arr)
del tmp[-2:]
tmp += "00"
arr = "".join(tmp)

for i in range(0, 100):
  if (int(arr)+i) % F == 0:
    del tmp[-2:]

    if i < 10: tmp += "0" + str(i)
    else: tmp += str(i)
    arr = "".join(tmp)

    print(arr[-2:])
    break