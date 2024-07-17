from sys import stdin
N = int(stdin.readline())
s = stdin.readline().strip()
ans = [ s[i*N:i*N+N] for i in range(len(s)//N)]
answer = ""
for i in range(len(ans[0])):
  for j in range(len(ans)):
    if j%2 == 0:
      answer += ans[j][i]
    else:
      answer += ans[j][::-1][i]
    
print(answer)  

