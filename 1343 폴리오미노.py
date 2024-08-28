from sys import stdin
A,B = 'AAAA', 'BB'
board = stdin.readline().strip()
answer = ""
X = 0
for i in range(len(board)):
  if board[i] == 'X': 
    X += 1
  if board[i] == '.' or i == len(board)-1:
    if X%2 == 1:
      answer = -1
      break
    if X >= 4 and X%2 == 0:  answer += A * (X//4)
    if X%4 == 2:             answer += B
    if board[i] == '.':      answer += '.'

    X = 0

print(answer)
  
