# @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다
#5355 화성수학
from sys import stdin

N = int(stdin.readline())
for _ in range(N):
	math = stdin.readline().strip().split(' ')
	num = float(math[0])
	for i in math[1:]:
		if i == '@': num *= 3
		elif i == '%': num += 5
		elif i == '#': num -= 7
	print("{:.2f}".format(num))
