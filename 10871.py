a, b = map(int, input().split())

c = [*map(int, input().split())]
if len(c) > a:
  del c[a:]

for i in c:
  if i < 1 or i > 10000:
    exit()

for i in c:
  if i < b:
    print(i, end=' ')