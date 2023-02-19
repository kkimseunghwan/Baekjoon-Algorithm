while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except:
    break

#try - except : 예외처리