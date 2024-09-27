
# 1269
from sys import stdin

# 각 집합의 원소의 개수는 200,000을 넘지 않으며
A, B = map(int, stdin.readline().split())

A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))

print(len((A-B)) + len((B-A)))

