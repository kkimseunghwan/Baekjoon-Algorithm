
# 1244 스위치 켜고 끄기
from sys import stdin

def changeSet(x):
	return 0 if x else 1

def ManSwitchSet(switch, start):
	for i in range(start-1, len(switch), start):
		switch[i] = changeSet(switch[i])

def WomanSwitchSet(switch, start):
	ran = start - 1 if len(switch)//2 >= start else  len(switch) - start
	switch[ start - 1 ] = changeSet(switch[ start - 1 ])
	
	for i in range(1, ran+1):
		if switch[ start - 1 - i ] != switch[ start - 1 + i]:
			break
		else:
			switch[ start - 1 - i ] = changeSet(switch[ start - 1 - i  ])	
			switch[ start - 1 + i ] = changeSet(switch[ start - 1 + i  ])

sw_cnt = int(stdin.readline()) # 1 <= N <= 100
switch = list(map(int, stdin.readline().split()))

S = int(stdin.readline()) # 1 <= N <= 100
for _ in range(S):
	gender, num = map(int, stdin.readline().split())
	if gender == 1:
		ManSwitchSet(switch, num)
	else:
		WomanSwitchSet(switch, num)

		
for i in range(1, len(switch)+1):
	print(switch[i-1], end=' ')
	if i%20 == 0:
		print()

