#1193 분수찾기
from sys import stdin
X = int(stdin.readline()) # X(1 ≤ X ≤ 10,000,000)
nowNum, index = 1, 1
while (nowNum + index - 1) < X:
  nowNum = nowNum + index
  index += 1
else:
  i = X - nowNum
  a, b = (1+i, index-i) if index%2==0 else (index-i, 1+i)
  print(f'{a}/{b}')

'''

시간 복잡도 이해를 위한 정리

#### 1. 그룹의 합산 패턴 분석

`index`가 증가하면서 `nowNum`도 증가하는 방식. nowNum은 각 그룹의 첫 번쨰 숫자
각 그룹의 크기는 `1, 2, 3, 4, ...`로 증가

ex)
-첫 번째 그룹: `1` (index 1)
-두 번째 그룹: `2, 3` (index 2)
-세 번째 그룹: `4, 5, 6` (index 3)
-...

`index`가 `n`일 때, 이 그룹의 마지막 숫자는 다음과 같이 계산

index*(index + 1) / 2
<< **중요** 문제 풀 때는 몰랐음..

이 값이 `X`를 넘어설 때까지 루프가 반복


반복 횟수

루프의 종료 조건 (nowNum + index - 1) >= X
이 때, nowNum은 각 그룹의 첫 번째 숫자. (nowNum + index - 1)는 각 그룹의 마지막 숫자.

각 `index`의 경우, `nowNum`은 `1 + 2 + 3 + ... + index`로 증가
이 합계는 *등차수열의 합*으로 계산


(≈ 는 근사치 라는 뜻)
index*(index + 1) / 2 ≈ X =>> index^2 ≈ 2X =>> index ≈ sqrt(2X)
(sqrt는 root를 뜻함)

`index`가 루프의 반복 횟수와 비례하기 때문에 
즉, 루프는 약 sqrt(X)번 반복된다.

따라서 코드의 전체 시간 복잡도는 O(sqrt(X))
- **sqrt(X)**는 `X`의 제곱근을 의미합니다.
- 만약 `X`가 최대 10,000,000이라면, `sqrt(10,000,000)`은 약 3,162 정도가 됩니다.

'''