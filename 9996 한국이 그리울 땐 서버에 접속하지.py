#9996
from sys import stdin

N = int(stdin.readline())

#패턴은 알파벳 소문자 여러 개와 별표(*) 하나로 이루어진 문자열이다.
#ad * a <- 이것도 된다는거같은데?

#문자열의 길이는 100을 넘지 않음
pattern_Front, pattern_Back = stdin.readline().strip().split('*')
len_front = len(pattern_Front)
len_back = len(pattern_Back)

for _ in range(N):
    file_name = stdin.readline().strip()
    if len(file_name) < (len_front + len_back):
        print("NE")
        continue
    if file_name[:len_front] == pattern_Front and file_name[-len_back:] == pattern_Back:
        print("DA")
    else:
        print("NE")