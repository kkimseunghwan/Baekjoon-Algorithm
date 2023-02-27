
case = int(input())
data = [*map(int, input().split())]
size = int(input())

disk = 0
for i in data:
    if i//size == 0 and i != 0:
      disk += 1
    elif i//size > 0:
       a = i//size
       while True:
          if size*a >= i: break
          a += 1
       disk += a

print(disk*size)



    



