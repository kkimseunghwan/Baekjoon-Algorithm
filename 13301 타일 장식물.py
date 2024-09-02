from sys import stdin

N = int(stdin.readline()) # N(1 ≤ N ≤ 80)
num1, num2, answer = 1, 1, 0

if N <= 1:
  answer = num1 * 4
else:
  for i in range(2, N):
    num1, num2 = num2, num1+num2
  answer = ((num1+num2) + num2) * 2
  
print(answer)