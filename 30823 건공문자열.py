from sys import stdin
N, K = map(int, stdin.readline().split())
text = list(stdin.readline().strip())

newText = text[K-1:]
if N%2 == 0:
    changeText = text[:K-1] if K%2 != 0 else list(reversed(text[:K-1]))
else:
    changeText = text[:K-1] if K%2 == 0 else list(reversed(text[:K-1]))
print(''.join(newText+changeText))
