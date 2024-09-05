#1026 보물

N = int(input()) #(1 <= N <= 50)
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse = True)

S = 0
for i in range(N):
  S += A[i] * B[i]

print(S)