#23971 ZOAC 4
from sys import stdin
H, W, N, M = map(int, stdin.readline().split())

a = H//(N+1) + (1 if H%(N+1) != 0 else 0)
b = W//(M+1) + (1 if W%(M+1) != 0 else 0)
print(a*b)

# 입력 받는 값이 4개로 정해져있으므로 O(1)
# 단순 사칙연산 및 조건문 O(1)
# 정수 출력 O(1)
# 시간복잡도 => O(1)

