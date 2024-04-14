N = int(input())
heghtList = list(map(int,input().split()))
answerList = []

for i in range(N-1, -1, -1):
    answerList.insert(heghtList[i], i+1)
    print("I", i, "answerList", answerList)

for i in answerList:
    print(i, end = " ")