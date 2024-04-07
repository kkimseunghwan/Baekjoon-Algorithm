height, width,  inventory = map(int, input().split()) # 세로 가로 인벤블록 값 입력
flotArr=[] # 각 위치별 땅의 높이 저장 리스트

for i in range(height): # 세로 길이 만큼 입력 반복
      flotArr.append(list(map(int,input().split()))) # 각 위치별 땅의 높이 입력

# 문제에서 블록의 좌표 값을 계산 후 출력하는 문제가 아니기 때문에
# (x, y, 높이) 3개의 값이 필요한 3차원 형태를
# 계산하기 편하도록 (x, 높이)의 2차원 형태로 변환하였다
flotArr = sum(flotArr, []) # ex) [[1,2], [3,4]] => [1,2,3,4]

# 목표로 할 평지 높이를 최소값으로 설정
blockToHigh = min(flotArr)

lastUseTime = 0 # 소요된 시간 이전 계산값 저장
for y in range(257):
    useTime = 0 # 소요된 시간
    lastB = inventory # 보유중인 블록 개수

    for i in flotArr: # 각 땅의 높이 검사
        if i == blockToHigh: continue # 목표 높이값과 같을경우 패스
        tempNum = abs(blockToHigh - i) # 목표높이와 현재높이의 차이값 저장
        if (i > blockToHigh): # 블럭이 목표 높이값보다 높을 경우 
            useTime += (tempNum * 2) # 소요 시간 증가
            lastB += tempNum # 인벤토리 블럭 추가
        else: # 블럭이 목표 높이값보다 낮을 경우 
            useTime += tempNum  # 소요 시간 증가
            lastB -= tempNum # 인벤토리 블럭 소모

    # 저장되어있는 이전 계산값이 존재하고
    # 방금 계산한 시간보다 이전 소요시간이 더 짧을경우
    # 혹은 인벤토리의 남은 블록 개수가 0보다 작을경우 게산 종료
    if lastUseTime != 0 and lastUseTime < useTime or lastB < 0: 
        useTime = lastUseTime # 소요 시간을 이전 소요시간으로 초기화
        blockToHigh -= 1 # 목표 설정한 높이을 이전 높이로 초기화
        break
    # 이전값과 소요시간이 동일할경우 목표높이값을 증가 시킨 후 검사 반복
    elif lastUseTime == useTime: blockToHigh += 1 
    elif blockToHigh == max(flotArr): break # 설정된 목표 높이값이 리스트의 값 중 최대값과 같을경우 게산 종료
    else: # 위의 조건을 모두 만족하지 않을 경우
        lastUseTime = useTime # 이전 소요시간을 방금 계산한 소요시간으로 초기화
        blockToHigh += 1 # 목표 높이값 증가

print(useTime, blockToHigh) # 소요시간 및 블록 높이 출력