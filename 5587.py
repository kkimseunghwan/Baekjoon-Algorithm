n = int(input()) #상근이에게 주어지는 카드의 개수
turn = True #turn 이 True일 시 상근이 차례, False일 시 근상이 차례
nowNum = 0 #현재 놓여진 카드의 숫자

#각 상근, 근상의 패
sangun = []

#상근이에게 주어질 카드
for i in range(n):
    a = int(input())
    sangun.append(a)

#보유 카드 중 가장 작은 수를 내기에, 오름차순 정렬
sangun.sort()
gunsang = [i for i in range(1,n*2+1) if i not in sangun]
#근상의 카드 = 2n개의 카드 중 상근이의 카드를 제외한 
#근상의 카드는 자동으로 정렬됨

#게임 시작
while sangun and gunsang: #상근과 근상의 리스트 값이 유효할 경우
    #만약 보유한 카드의 개수가 0장이 된 사람이 나올 시 게임 종료
    if turn: #상근이 턴
        turn = False #근상이 턴으로 변경
        for i in sangun:
            if nowNum < i: #만약 놓여진 카드의 수보다 큰 숫자를 가지고 있을 시
                nowNum = i #놓여진 카드를 상근이의 카드로 변경
                sangun.remove(i) #상근이의 카드를 삭제
                break #for문 탈출
        if nowNum != i: #상근이가 카드를 내지 못했을 경우
            nowNum = 0 #놓여진 카드를 초기화
    else: #근상이 턴 위와 같음
        turn = True
        for j in gunsang:
            if nowNum < j: 
                nowNum = j 
                gunsang.remove(j) 
                break
        if nowNum != j:
            nowNum = 0 

#점수 = 상대의 남은 패
print(len(gunsang))
print(len(sangun))    
