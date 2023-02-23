love = ['L', 'O', 'V', 'E'] #대상 단어
name = input() #이름 입력 받기

team = [] #팀 이름 저장 공간
for i in range(int(input())):
  team.append(input()) #팀 이름 입력
team.sort() #오름차순 정렬

winteam = [] #계산 결과를 저장 할 공간
for i in range(len(team)): #저장 할 개수는 팀 개수만큼
  c = [ name.count(i) for i in love ] # 이름에서 개수 계산
  for j in range(len(love)): #비교할 단어의 길이만큼 반복
    c[j] += team[i].count(love[j])
  #max = 1
  #for p in range(0, len(love)-1):
  #  for q in range(p+1, len(love)):
  #    max *= (c[p]+c[q])
  #print(max)
  #winteam.append(max%100)
  winteam.append( ((c[0]+c[1])*(c[0]+c[2])*(c[0]+c[3])*(c[1]+c[2])*(c[1]+c[3])*(c[2]+c[3]))%100 )
  #((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100

print(team[winteam.index(max(winteam))])