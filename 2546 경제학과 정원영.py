tcase = int(stdin.readline())
for _ in range(tcase):
  stdin.readline()
  N, M = map(int, stdin.readline().split())
  Nl = list(map(int, stdin.readline().split()))
  Ns = sum(Nl)
  Ms = sum(map(int, stdin.readline().split()))
  cnt = 0
  for i in Nl:
    if i*N < Ns and i*M > Ms: 
      cnt += 1
  print(cnt)
