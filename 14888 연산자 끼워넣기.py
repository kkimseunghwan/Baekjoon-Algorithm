
from sys import stdin

# 수의 개수 N(2 ≤ N ≤ 11)
N = int(stdin.readline())

# 수의 값
num = list(map(int, stdin.readline().split()))

# 차례대로 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)의 개수
operater = list(map(int, stdin.readline().split()))

#print(N, num, operater)

answer = []

def OperaterBackTracking(numList, index, value,  oper):
	# 마지막 값까지 연산 시, 값을 리스트에 저장
	if len(numList) == index:
		answer.append(value)
		return
	
	if oper[0]:
		newOper = oper[:]
		newOper[0] -= 1
		OperaterBackTracking(numList, index+1, value+numList[index], newOper)
	
	if oper[1]:
		newOper = oper[:]
		newOper[1] -= 1
		OperaterBackTracking(numList, index+1, value-numList[index], newOper)
	
	if oper[2]:
		newOper = oper[:]
		newOper[2] -= 1
		OperaterBackTracking(numList, index+1, value*numList[index], newOper)
		
	if oper[3]:
		newOper = oper[:]
		newOper[3] -= 1
		val = value
		value = abs(value)//numList[index]
		if val < 0:
			value *= -1
		OperaterBackTracking(numList, index+1, value, newOper)
	

OperaterBackTracking(num, 1, num[0], operater)
#print(answer)
print(max(answer))
print(min(answer))
		


