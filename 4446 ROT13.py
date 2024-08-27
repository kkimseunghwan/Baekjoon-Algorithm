
############# 입력은 여러 줄로 이루어져 있다. #############
# EOF 써야됨

a = 'aiyeou'
al = 6
b = 'bkxznhdcwgpvjqtsrlmf'
bl = 20

try:
  while True: # EOF 중지 전 까지 여러번 입력 가능 O(L)

    text = input()
    ROT13 = ""

    for i in text: # 입력 길이에 따라 반복 O(N)
      isUp = False
      if i.isupper(): 
        i = i.lower()
        isUp = True

      if i in a: # 고정된 크기 값 내에서 검사 O(1)
        str_index = a.find(i)-3 # 고정된 크기 값 내에서 검사 O(1)
        i = a[str_index] if str_index >= 0 else a[al + str_index]
      elif i in b: # 위와 동일
        str_index = b.find(i)-10
        i = b[str_index] if str_index >= 0 else b[bl + str_index]
      if isUp: i = i.upper()
      ROT13 += i

    print(ROT13)
except EOFError:
  exit()

# O(L * N)