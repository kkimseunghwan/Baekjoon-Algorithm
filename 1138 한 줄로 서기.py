N = int(input())
heghtList = list(map(int,input().split()))

answerList = []
for i in range(N):
    answerList.append(N)

case = 0

while case + 1 != N:
    if case == 0:
        answerList[heghtList[0]] = 1
        case += 1
        continue
    else:
        for i in range(N):
            leftCount = answerList[:i].count(N)
            if heghtList[case] == leftCount and answerList[i] == N:
                answerList[i] = case+1
                case += 1
                break

for i in answerList:
    print(i, end = " ")