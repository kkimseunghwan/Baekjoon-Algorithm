
fivo = [1, 1] #피보나치 수열을 저장할 리스트
answer = [] #출력할 답을 저장할 리스트

for i in range(int(input())): #테스트 케이스 횟수 설정
    P, Q = map(int, input().split()) #P와 Q 입력 (P번째 피보나치 숫자를 Q로 나눈 나머지를 계산하여야 함) 

    if len(fivo) < P: #만약 현재 저장되어있는 피보나치 리스트의 길이가 P값보다 작을 경우
        while len(fivo) < P:
            p = len(fivo) #피보나치 리스트의 마지막 데이터 저장
            fivoNum = fivo[p-1] + fivo[p-2] #리스트의 다음 값 피보나치 수로 계산
            fivo.append(fivoNum) #계산한 피보나치 수열을 리스트에 저장
    else: #만약 현재 저장되어있는 피보나치 리스트의 길이가 P값보다 클 경우 (추가 계산 필요없음)
        fivoNum = fivo[P-1] #정의 되어있는 피보나치 리스트에서 P번째의 피보나치 숫자 저장 

    answer.append(fivoNum % Q) #구해야 할 값인 피보나치 숫자를 Q로 나눈 나머지 저장

#결과 값 출력
for i in range(len(answer)):
    print("Case #%d:" %(i+1), answer[i])

