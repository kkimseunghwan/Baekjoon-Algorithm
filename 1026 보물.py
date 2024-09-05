#1026 보물

N = int(input()) #(1 <= N <= 50)
keys = list(range(0,N))
dictA = dict(zip(keys, sorted(list(map(int, input().split())))))
dictB = dict(zip(keys, sorted(list(map(int, input().split())), reverse = True)))

S = 0
for i in range(N):
  S += dictA[i] * dictB[i]

print(S)
