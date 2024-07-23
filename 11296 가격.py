#11296 가격
from sys import stdin
import math

def Dot(p, c):
  if c == 'R': return p - (p * 0.45)
  elif c == 'G': return p - (p * 0.30)
  elif c == 'B': return p - (p * 0.20)
  elif c == 'Y': return p - (p * 0.15)
  elif c == 'O': return p - (p * 0.10)
  else: return p - (p * 0.05)
    
def Coupon(p, b):
  if b == 'C':
    return p - (p * 0.05)
  else:
    return p
    
def Cash(p,c):
  if c == 'C':
    a,b = str(p).split('.')
    if len(b) > 1 and b[1] == '5':
      return p - 0.05
    else:
      return round(p, 1)
  else:
    return round(p, 2)
  
N = int(stdin.readline())
for _ in range(N):
  price, dots, coupon, buy = map(str, stdin.readline().split())
  print("${:.2f}".format(Cash(Coupon(Dot(float(price), dots), coupon), buy)))
