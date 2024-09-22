from sys import stdin
import math

N = int(stdin.readline()) # 토핑의 종류의 수 N(1 ≤ N ≤ 100)

# 도우의 가격 A와 토핑의 가격 B가 주어진다. (1 ≤ A, B ≤ 1000) 
d_price, t_price = map(int, stdin.readline().split()) 
d_cal = int(stdin.readline()) # 도우의 열량 (1 ≤ C ≤ 10000) 

t_cal = []
for _ in range(N):
    t_cal.append(int(stdin.readline()))

for cal in sorted(t_cal, reverse=True):
    if d_cal / d_price < cal / t_price:
        d_cal += cal
        d_price += t_price

print( math.floor(d_cal / d_price))



