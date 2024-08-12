def Kantoer(dash, N):
  a = N // 3
  if a == 0:
    return dash
  return Kantoer(dash[:a], a) + (' ' * a) + Kantoer(dash[:a], a)

while True:
  try:
    N = 3 ** int(input())
    print(Kantoer('-' * N, N))
  except EOFError:
    break
  