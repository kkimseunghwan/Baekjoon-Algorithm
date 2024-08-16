from sys import stdin
btn = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
num = list(map(int, stdin.readline().split()))
message = stdin.readline().strip()

answer = ""
for i in message:
  for k in range(len(btn)):
    if i in btn[k]:
      index = btn[k].index(i) + 1
      n = str(num.index(k+2)+1)
      if len(answer) > 0 and answer[-1] == n:
        answer += '#'
      answer += n * index
      
print(answer)