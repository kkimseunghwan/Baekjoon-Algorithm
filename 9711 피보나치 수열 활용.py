
fivo = [1, 1]
answer = []
for i in range(int(input())):
    P, Q = map(int, input().split())

    fivoNum = 0
    if len(fivo) >= P:
        fivoNum = fivo[P-1]
    else:
        while len(fivo) < P:
            p = len(fivo)
            fivoNum = fivo[p-1] + fivo[p-2]
            fivo.append(fivoNum)
    answer.append(fivoNum % Q)

print(fivo)

for i in range(len(answer)):
    print("Case #%d:" %(i+1), answer[i])

