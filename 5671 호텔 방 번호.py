try:
  while True: # O(L)
    cnt = 0
    N, M = map(int, input().split()) # (1 ≤ N ≤ M ≤ 5000)
    for i in range(N, M+1): # 최대 5000번 반복 O(N)
      for j in str(i): # 숫자의 각 자리수 검사. 최대 4자리. O(1)
        if str(i).count(j) > 1: # 숫자의 각 자리수가 중복된 경우. O(1) 최대 O(16)
          break
      else:
        cnt += 1
    print(cnt)
except EOFError:
  exit()

# O(L * N)