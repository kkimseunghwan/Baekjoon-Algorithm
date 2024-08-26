#25206 너의평점은
from sys import stdin
score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sub_Score, all_Score = 0, 0
for _ in range(20):
  a,b,c = stdin.readline().strip().split()
  if c != 'P':
    all_Score += float(b)
    sub_Score += float(b) * score[c]
else:
  print("{:.6f}".format(sub_Score / all_Score))

# 시간 복잡도 O(1)
# 입력 데이터 크기와 관계없이 20번의 고정된 횟수만큼 반복




