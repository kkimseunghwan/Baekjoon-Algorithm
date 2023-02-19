case = int(input())

for i in range(case):
  a, b = map(int, input().split())

  x = a%10
  y = (b%4 if b%4 != 0 else 4)

  print( str(x**y)[-1] if x**y != 0 else "10")
    

