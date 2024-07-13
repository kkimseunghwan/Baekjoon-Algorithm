from sys import stdin
X = int(stdin.readline())
stick = [64]
cnt = 0
while sum(stick) > X:
    m = min(stick)
    stick.remove(m)
    stick.append(m//2)
    cnt += 1
    if sum(stick) >= X:
        continue
    elif sum(stick) < X:
        stick.append(m//2)
    
print(len(stick))


