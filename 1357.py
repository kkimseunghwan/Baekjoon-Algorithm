
A, B = map(str, input().split())

def Ren(val):
    a = ""
    for i in range(len(val)-1, -1, -1):
      a += val[i]
    return int(a)

print(Ren(str(Ren(A)+ Ren(B))))

