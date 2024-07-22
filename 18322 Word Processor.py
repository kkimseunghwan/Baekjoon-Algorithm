#18322 Word Processor
from sys import stdin
N, K = map(int, stdin.readline().split())
words = list(map(str, stdin.readline().split()))
out = ""
while words:
  if len((out + words[0]).replace(" ", "")) <= K:
    out += words[0] if len(out) == 0 else " " + words[0]
    del words[0]
  else:
    print(out)
    out = ""
else:
  print(out)